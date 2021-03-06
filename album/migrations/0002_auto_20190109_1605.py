# Generated by Django 2.1.4 on 2019-01-09 08:05

import album.models
from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='introduction',
            field=models.TextField(max_length=256),
        ),
        migrations.AlterField(
            model_name='album',
            name='thumb',
            field=imagekit.models.fields.ProcessedImageField(upload_to=album.models.getUploadPath),
        ),
        migrations.AlterField(
            model_name='albumimage',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(upload_to=album.models.getUploadPath),
        ),
    ]
