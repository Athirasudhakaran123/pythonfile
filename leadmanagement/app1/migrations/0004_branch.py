# Generated by Django 4.2.7 on 2023-11-18 09:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app1', '0003_alter_district_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('isactive', models.BooleanField(default=True, verbose_name='active')),
                ('branch', models.CharField(max_length=200)),
                ('Branch_code', models.CharField(max_length=50, null=True, unique=True)),
                ('adress', models.CharField(blank=True, max_length=500)),
                ('street', models.CharField(blank=True, max_length=200)),
                ('pincode', models.PositiveIntegerField(blank=True, null=True)),
                ('mobile', models.CharField(max_length=12)),
                ('email', models.EmailField(blank=True, max_length=200)),
                ('created_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('district', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='state', chained_model_field='state', limit_choices_to={'isactive': True}, on_delete=django.db.models.deletion.CASCADE, to='app1.district')),
                ('state', models.ForeignKey(limit_choices_to={'isactive': True}, on_delete=django.db.models.deletion.CASCADE, to='app1.state')),
            ],
            options={
                'verbose_name_plural': 'Branches',
                'ordering': ('state', 'district'),
            },
        ),
    ]
