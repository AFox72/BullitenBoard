# Generated by Django 4.1.5 on 2023-01-18 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Board', '0002_rename_comment_reply_rename_category_post_categories_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='Board.post'),
        ),
    ]