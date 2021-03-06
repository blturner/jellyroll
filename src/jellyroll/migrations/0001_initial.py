# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-15 03:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import tagging.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=1000, unique=True)),
                ('description', models.CharField(max_length=255)),
                ('extended', models.TextField(blank=True)),
                ('thumbnail', models.ImageField(blank=True, upload_to=b'img/jellyroll/bookmarks/%Y/%m')),
                ('thumbnail_url', models.URLField(blank=True, max_length=1000)),
                ('to_read', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CodeCommit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('revision', models.CharField(max_length=200)),
                ('message', models.TextField()),
            ],
            options={
                'ordering': ['-revision'],
            },
        ),
        migrations.CreateModel(
            name='CodeRepository',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[(b'svn', b'Subversion'), (b'git', b'Git')], max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('username', models.CharField(help_text=b'Your username/email for this SCM.', max_length=100)),
                ('public_changeset_template', models.URLField(blank=True, help_text=b"Template for viewing a changeset publically. Use '%s' for the revision number")),
                ('url', models.URLField()),
            ],
            options={
                'verbose_name_plural': 'code repositories',
            },
        ),
        migrations.CreateModel(
            name='ContentLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('identifier', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.TextField()),
                ('url', models.URLField(blank=True, max_length=1000)),
                ('timestamp', models.DateTimeField()),
                ('tags', tagging.fields.TagField(blank=True, max_length=2500)),
                ('source', models.CharField(blank=True, max_length=100)),
                ('source_id', models.TextField(blank=True)),
                ('object_str', models.TextField(blank=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=10)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=10)),
                ('name', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('links', models.ManyToManyField(blank=True, null=True, to='jellyroll.ContentLink')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('photo_id', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('farm_id', models.PositiveSmallIntegerField(null=True)),
                ('server_id', models.PositiveSmallIntegerField()),
                ('secret', models.CharField(blank=True, max_length=30)),
                ('taken_by', models.CharField(blank=True, max_length=100)),
                ('cc_license', models.URLField(blank=True, choices=[(b'http://creativecommons.org/licenses/by/2.0/', b'CC Attribution'), (b'http://creativecommons.org/licenses/by-nd/2.0/', b'CC Attribution-NoDerivs'), (b'http://creativecommons.org/licenses/by-nc-nd/2.0/', b'CC Attribution-NonCommercial-NoDerivs'), (b'http://creativecommons.org/licenses/by-nc/2.0/', b'CC Attribution-NonCommercial'), (b'http://creativecommons.org/licenses/by-nc-sa/2.0/', b'CC Attribution-NonCommercial-ShareAlike'), (b'http://creativecommons.org/licenses/by-sa/2.0/', b'CC Attribution-ShareAlike')])),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True)),
                ('comment_count', models.PositiveIntegerField(default=0, max_length=5)),
                ('date_uploaded', models.DateTimeField(blank=True, null=True)),
                ('date_updated', models.DateTimeField(blank=True, null=True)),
                ('_exif', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='SearchEngine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('home', models.URLField()),
                ('search_template', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_name', models.CharField(max_length=250)),
                ('track_name', models.CharField(max_length=250)),
                ('url', models.URLField(blank=True, max_length=1000)),
                ('track_mbid', models.CharField(blank=True, max_length=36, verbose_name=b'MusicBrainz Track ID')),
                ('artist_mbid', models.CharField(blank=True, max_length=36, verbose_name=b'MusicBrainz Artist ID')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='VideoSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('home', models.URLField()),
                ('embed_template', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='WebSearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.CharField(max_length=250)),
                ('engine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='searches', to='jellyroll.SearchEngine')),
            ],
            options={
                'verbose_name_plural': 'web searches',
            },
        ),
        migrations.CreateModel(
            name='WebSearchResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('url', models.URLField()),
                ('search', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='jellyroll.WebSearch')),
            ],
        ),
        migrations.AddField(
            model_name='video',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='jellyroll.VideoSource'),
        ),
        migrations.AddField(
            model_name='codecommit',
            name='repository',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commits', to='jellyroll.CodeRepository'),
        ),
        migrations.AlterUniqueTogether(
            name='item',
            unique_together=set([('content_type', 'object_id')]),
        ),
    ]
