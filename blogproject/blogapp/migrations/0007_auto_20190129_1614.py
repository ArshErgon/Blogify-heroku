# Generated by Django 2.1.5 on 2019-01-29 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0006_popular_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='popular_post',
            old_name='popular_post',
            new_name='popular_posts',
        ),
    ]
