# Generated by Django 2.1.5 on 2019-01-29 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='owner_message',
            field=models.TextField(blank=True, default='Some message'),
        ),
    ]
