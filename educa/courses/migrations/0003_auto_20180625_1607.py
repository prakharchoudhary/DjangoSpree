# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import courses.fields


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_content_file_image_text_video'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='content',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='module',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='content',
            name='order',
            field=courses.fields.OrderField(default=0, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='module',
            name='order',
            field=courses.fields.OrderField(default=0, blank=True),
            preserve_default=False,
        ),
    ]
