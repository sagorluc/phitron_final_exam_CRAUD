# Generated by Django 4.2.4 on 2023-09-01 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_app', '0006_alter_crudmodel_image_delete_profilemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crudmodel',
            name='image',
            field=models.ImageField(default='photo.jpg', null=True, upload_to='photos/images'),
        ),
    ]
