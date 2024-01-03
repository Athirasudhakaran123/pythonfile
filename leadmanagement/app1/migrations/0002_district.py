# Generated by Django 4.2.7 on 2023-11-10 09:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='district',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('isactive', models.BooleanField(default=True, verbose_name='active')),
                ('districtname', models.CharField(max_length=100, unique=True)),
                ('created_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('state', models.ForeignKey(limit_choices_to={'isactive': True}, on_delete=django.db.models.deletion.CASCADE, to='app1.state')),
            ],
            options={
                'ordering': ['-isactive'],
                'abstract': False,
            },
        ),
    ]