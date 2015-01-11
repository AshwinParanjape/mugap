from django.db import models
from django.core.files.storage import FileSystemStorage
#fs = FileSystemStorage(location='/media/')


class Publication(models.Model):
    cluster_id = models.CharField(max_length = 50, primary_key=True)
    excerpt = models.TextField(null = True)
    num_citations = models.IntegerField(null = True)
    num_versions = models.IntegerField(null = True)
    title = models.TextField(null = True)
    second_line = models.TextField(null=True)
    url = models.TextField(null = True)
    url_citations = models.TextField(null = True)
    url_pdf = models.TextField()
    url_versions = models.TextField(null = True)
    year = models.IntegerField(null = True)
    pdf_file = models.FileField(upload_to = "pdf/")

    def get_peerstand_url(self):
        "A blog will redirect to the original post"
        #if self.url:
        #    return self.url
        return '/pdf/'+self.cluster_id+'/'


class Annotation(models.Model):
    cluster = models.ForeignKey(Publication)
    page_num = models.IntegerField(null = True)
    post = models.ForeignKey('posts.Post')
    annotated_text = models.TextField()
    serialized_version = models.TextField()
    def json_for_pdf(self):
		return dict( page_num=self.page_num, post=self.post.id, annotated_text=self.annotated_text, serialized_version=self.serialized_version)
