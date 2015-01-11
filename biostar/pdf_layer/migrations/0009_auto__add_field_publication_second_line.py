# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Publication.second_line'
        db.add_column(u'pdf_layer_publication', 'second_line',
                      self.gf('django.db.models.fields.TextField')(null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Publication.second_line'
        db.delete_column(u'pdf_layer_publication', 'second_line')


    models = {
        u'pdf_layer.annotation': {
            'Meta': {'object_name': 'Annotation'},
            'annotated_text': ('django.db.models.fields.TextField', [], {}),
            'cluster': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pdf_layer.Publication']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page_num': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['posts.Post']"}),
            'serialized_version': ('django.db.models.fields.TextField', [], {})
        },
        u'pdf_layer.publication': {
            'Meta': {'object_name': 'Publication'},
            'cluster_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'excerpt': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'num_citations': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'num_versions': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'pdf_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'second_line': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'url': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'url_citations': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'url_pdf': ('django.db.models.fields.TextField', [], {}),
            'url_versions': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        u'posts.post': {
            'Meta': {'object_name': 'Post'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.User']"}),
            'book_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'changed': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'comment_count': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'default': "u''"}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'has_accepted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'html': ('django.db.models.fields.TextField', [], {'default': "u''"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastedit_date': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'lastedit_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'editor'", 'to': u"orm['users.User']"}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'children'", 'null': 'True', 'to': u"orm['posts.Post']"}),
            'rank': ('django.db.models.fields.FloatField', [], {'default': '0', 'blank': 'True'}),
            'reply_count': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'root': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'descendants'", 'null': 'True', 'to': u"orm['posts.Post']"}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']", 'null': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'sticky': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'subs_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'tag_set': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['posts.Tag']", 'symmetrical': 'False', 'blank': 'True'}),
            'tag_val': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '100', 'blank': 'True'}),
            'thread_score': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'type': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'view_count': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'vote_count': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True', 'blank': 'True'})
        },
        u'posts.tag': {
            'Meta': {'object_name': 'Tag'},
            'count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'max_length': '50', 'db_index': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'users.user': {
            'Meta': {'object_name': 'User'},
            'activity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'badges': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'flair': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '15'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255'}),
            'new_messages': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']", 'null': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'type': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['pdf_layer']