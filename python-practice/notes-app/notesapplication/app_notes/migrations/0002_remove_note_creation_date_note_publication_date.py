# Generated by Django 5.0 on 2024-04-30 10:52

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_notes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='creation_date',
        ),
        migrations.AddField(
            model_name='note',
            name='publication_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
