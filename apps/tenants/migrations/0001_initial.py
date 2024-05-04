# Generated by Django 5.0.4 on 2024-05-04 05:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('rating_user', models.PositiveIntegerField(default=0)),
                ('phone', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'Inquilino',
                'verbose_name_plural': 'Inquilinos',
            },
        ),
    ]
