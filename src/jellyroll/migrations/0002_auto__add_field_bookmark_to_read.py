# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Bookmark.to_read'
        db.add_column('jellyroll_bookmark', 'to_read',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Bookmark.to_read'
        db.delete_column('jellyroll_bookmark', 'to_read')


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'jellyroll.bookmark': {
            'Meta': {'object_name': 'Bookmark'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'extended': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'thumbnail_url': ('django.db.models.fields.URLField', [], {'max_length': '1000', 'blank': 'True'}),
            'to_read': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'url': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '1000'})
        },
        'jellyroll.codecommit': {
            'Meta': {'ordering': "['-revision']", 'object_name': 'CodeCommit'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'repository': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'commits'", 'to': "orm['jellyroll.CodeRepository']"}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'jellyroll.coderepository': {
            'Meta': {'object_name': 'CodeRepository'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'public_changeset_template': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'jellyroll.contentlink': {
            'Meta': {'object_name': 'ContentLink'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'jellyroll.item': {
            'Meta': {'ordering': "['-timestamp']", 'unique_together': "[('content_type', 'object_id')]", 'object_name': 'Item'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.TextField', [], {}),
            'object_str': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'source_id': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'tags': ('tagging.fields.TagField', [], {'max_length': '2500'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '1000', 'blank': 'True'})
        },
        'jellyroll.location': {
            'Meta': {'object_name': 'Location'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '6'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '6'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        'jellyroll.message': {
            'Meta': {'object_name': 'Message'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'links': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['jellyroll.ContentLink']", 'null': 'True', 'blank': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {})
        },
        'jellyroll.photo': {
            'Meta': {'object_name': 'Photo'},
            '_exif': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'cc_license': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'comment_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'max_length': '5'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_uploaded': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'farm_id': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'photo_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50', 'primary_key': 'True'}),
            'secret': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'server_id': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'taken_by': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'jellyroll.searchengine': {
            'Meta': {'object_name': 'SearchEngine'},
            'home': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'search_template': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'jellyroll.track': {
            'Meta': {'object_name': 'Track'},
            'artist_mbid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'artist_name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'track_mbid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'track_name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '1000', 'blank': 'True'})
        },
        'jellyroll.video': {
            'Meta': {'object_name': 'Video'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'videos'", 'to': "orm['jellyroll.VideoSource']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'jellyroll.videosource': {
            'Meta': {'object_name': 'VideoSource'},
            'embed_template': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'home': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'jellyroll.websearch': {
            'Meta': {'object_name': 'WebSearch'},
            'engine': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'searches'", 'to': "orm['jellyroll.SearchEngine']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'query': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'jellyroll.websearchresult': {
            'Meta': {'object_name': 'WebSearchResult'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'search': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'results'", 'to': "orm['jellyroll.WebSearch']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['jellyroll']