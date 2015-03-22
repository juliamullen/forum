# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_post_date', models.DateTimeField(verbose_name=b'date of last post')),
                ('post_count', models.IntegerField()),
                ('title', models.CharField(max_length=50, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=25)),
                ('text', models.TextField()),
                ('date', models.DateTimeField(verbose_name=b'date published')),
                ('image', models.ImageField(upload_to=b'img/%d', blank=True)),
                ('conversation', models.ForeignKey(to='conversation.Conversation')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='conversation',
            name='forum',
            field=models.ForeignKey(to='conversation.Place'),
            preserve_default=True,
        ),
    ]
