# Generated by Django 4.2.7 on 2023-12-05 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_remove_students_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='ph',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
