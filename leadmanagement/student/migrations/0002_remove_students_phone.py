# Generated by Django 4.2.7 on 2023-12-05 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='phone',
        ),
    ]