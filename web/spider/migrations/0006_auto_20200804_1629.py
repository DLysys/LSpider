# Generated by Django 3.0.7 on 2020-08-04 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spider', '0005_auto_20200423_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subdomainlist',
            name='subdomain',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='urltable',
            name='url',
            field=models.CharField(max_length=2000),
        ),
    ]
