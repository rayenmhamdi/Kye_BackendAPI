# Generated by Django 3.1.4 on 2020-12-27 10:50
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_auto_20201227_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='date_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='supplier',
            name='date_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
