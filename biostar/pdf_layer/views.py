from django.shortcuts import render
from biostar.pdf_layer.models import Publication, Annotation
from scholar import *
import urllib
from django.core.files import File
import os
import json
from django.http import HttpResponse
from django.forms.models import model_to_dict
from django.core import serializers
from biostar.server import views
from biostar.apps.posts.models import Post


def posts_by_cluster_id(request, cluster_id):
	post_ids = Annotation.objects.filter(cluster=cluster_id).values_list('post', flat=True)
	#posts = Annotation.objects.filter(cluster=cluster_id).select_related('post')
	return Post.objects.filter(id__in = post_ids)



class DocumentPostList(views.PostList):
    def get_title(self):
		cluster_id = self.kwargs.get("cluster_id", "")
		pub =  Publication.objects.get(cluster_id = cluster_id)
		self.topic = pub.title
		self.topic = "Publication"

    def get_queryset(self):
		cluster_id = self.kwargs.get("cluster_id", "")
		print cluster_id
		pub =  Publication.objects.get(cluster_id = cluster_id)
		self.topic = pub.title
		
		query = posts_by_cluster_id(self.request, cluster_id)
		query = views.apply_sort(self.request, query)

        # Limit latest topics to a few pages.
		if not self.topic:
			query = query[:settings.SITE_LATEST_POST_LIMIT]
		return query


# Create your views here.
def get_annotations(request, cluster_id):
	#json_response_data = serializers.serialize('json',Annotation.objects.filter(cluster=cluster_id))
	json_response_data = [ob.json_for_pdf() for ob in Annotation.objects.filter(cluster=cluster_id)]
	return HttpResponse(json.dumps(json_response_data), content_type="application/json")

def pdf_viewer(request):
	if 'cluster_id' in request.GET:
		get_dict = request.GET.copy()
		get_dict.update({'file':'media/pdf/'+request.GET['cluster_id']+'.pdf'})
		request.GET= get_dict
		return render(request, "pdf_viewer.html", {'cluster_id':request.GET['cluster_id']})

def pdf_interface(request, cluster_id):
	if cluster_id:
		p = Publication.objects.get(cluster_id = cluster_id)
		if not p.pdf_file:
			(filename, headers) = urllib.urlretrieve(p.url_pdf)
			print filename
			f = open(filename)
			f1 = File(f)
			p.pdf_file.save(p.cluster_id+'.pdf', f1)
			print p.pdf_file.name
			p.save()
		else: 
			print p.title, p.url_pdf
        get_dict = request.GET.copy()
        get_dict.update({'file':'media/pdf/'+p.cluster_id+'.pdf'})
        request.GET= get_dict

        r = render(request, "pdf_interface.html", {'cluster_id':p.cluster_id, 'title':p.title})
        return r

def pub_search(request):
	error = False
	if 'q' in request.GET:
		q = request.GET['q']
		if not q:
			error = True
		else:
			query = SearchScholarQuery()
			query.set_words(q)
			querier = ScholarQuerier()
			querier.send_query(query)
			
			for article_1 in querier.articles:
				article = article_1.attrs
				if article['url_pdf'][0] is not None:
					p = Publication(cluster_id = article['cluster_id'][0],
							excerpt = article['excerpt'][0],
							num_citations = article['num_citations'][0],
							num_versions = article['num_versions'][0],
							title = article['title'][0],
                                                        second_line = article['second_line'][0],
							url = article['url'][0],
							url_citations = article['url_citations'][0],
							url_pdf = article['url_pdf'][0],
							url_versions = article['url_versions'][0],
					#		year = int(article['year'][0]),
							)
							
					print p.title
					print p.url_pdf
                                        print p.second_line
					p.save()

			print([(e.cluster_id, e.title, e.url_pdf) for e in Publication.objects.all()])
                        #TODO:Save data
			return render(request, 'pub_search_results.html', {'articles': [article.attrs for article in querier.articles], 'query': q})
	return render(request, 'pub_search_form.html', {'error': error})


