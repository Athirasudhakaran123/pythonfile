# Generated by Django 4.2.7 on 2023-12-07 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_batch_batch'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='end_time',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='batch',
            name='start_time',
            field=models.TimeField(null=True),
        ),
    ]
