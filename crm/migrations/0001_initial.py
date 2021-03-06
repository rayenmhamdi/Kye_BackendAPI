# Generated by Django 3.1.4 on 2020-12-27 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_1', models.PositiveIntegerField(blank=True, null=True)),
                ('phone_2', models.PositiveIntegerField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('purchase_number', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_1', models.PositiveIntegerField(blank=True, null=True)),
                ('phone_2', models.PositiveIntegerField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('supply_number', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
