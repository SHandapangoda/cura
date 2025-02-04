# Generated by Django 5.1.5 on 2025-02-04 08:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('care_provider', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CareSeeker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preferences', models.JSONField(default=dict)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='care_seeker', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tasks', models.JSONField(default=list)),
                ('status', models.CharField(default='PENDING', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('care_provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='care_provider.careprovider')),
                ('care_seeker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='care_seeker.careseeker')),
            ],
        ),
    ]
