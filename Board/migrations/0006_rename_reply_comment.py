# Generated by Django 4.1.5 on 2023-01-18 17:12

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Board', '0005_alter_post_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reply',
            new_name='Comment',
        ),
    ]
