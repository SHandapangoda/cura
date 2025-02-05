# Generated by Django 5.1.5 on 2025-02-04 08:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CareProvider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience', models.TextField(blank=True, null=True)),
                ('education', models.TextField(blank=True, null=True)),
                ('tasks', models.JSONField(default=list)),
                ('is_available', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='care_provider', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
