# Generated by Django 3.1.2 on 2020-11-19 16:04

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201119_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='Post',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='Title',
            field=models.CharField(max_length=100),
        ),
    ]