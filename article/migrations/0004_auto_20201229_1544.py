# Generated by Django 3.1.4 on 2020-12-29 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20201229_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='code',
            field=models.CharField(max_length=3, unique=True),
        ),
    ]
