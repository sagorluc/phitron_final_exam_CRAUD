# Generated by Django 4.2.4 on 2023-09-01 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_app', '0003_profilemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='profile_image',
            field=models.ImageField(blank=True, default='photos/images/photo.jpg', upload_to='photos/images'),
        ),
    ]