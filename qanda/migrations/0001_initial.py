# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('postdate', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField()),
                ('content', models.TextField()),
                ('postdate', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=65)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('login', models.CharField(max_length=145)),
                ('pwd', models.CharField(max_length=145)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='question',
            name='likes',
            field=models.ManyToManyField(related_name=b'question_likes', to='qanda.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(related_name=b'question_tags', to='qanda.Tag'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='question',
            name='user_iduser',
            field=models.ForeignKey(to='qanda.User', db_column=b'user_iduser'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='likes',
            field=models.ManyToManyField(related_name=b'answer_likes', to='qanda.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='question_idquestion',
            field=models.ForeignKey(to='qanda.Question', db_column=b'question_idquestion'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='user_iduser',
            field=models.ForeignKey(to='qanda.User', db_column=b'user_iduser'),
            preserve_default=True,
        ),
    ]
