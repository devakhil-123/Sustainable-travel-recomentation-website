# Generated by Django 5.0 on 2024-04-24 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_remove_bicyclemodel_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='accomodation',
            name='img2',
            field=models.ImageField(null=True, upload_to='accomodation_images'),
        ),
    ]
