# Generated by Django 4.2.11 on 2024-04-15 03:24

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0006_friends'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Friends',
            new_name='Friend',
        ),
    ]
