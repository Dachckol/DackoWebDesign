# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20141217_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactentry',
            name='email',
            field=models.EmailField(max_length=100),
            preserve_default=True,
        ),
    ]
