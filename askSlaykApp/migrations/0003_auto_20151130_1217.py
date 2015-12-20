# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('askSlaykApp', '0002_auto_20151130_1147'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(default=b'')),
                ('rating', models.IntegerField(default=0)),
                ('question', models.ForeignKey(to='askSlaykApp.Question')),
                ('user', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='answeer',
            name='question',
        ),
        migrations.RemoveField(
            model_name='answeer',
            name='user',
        ),
        migrations.DeleteModel(
            name='Answeer',
        ),
    ]
