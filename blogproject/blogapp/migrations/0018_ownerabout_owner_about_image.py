# Generated by Django 2.1.5 on 2019-01-29 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0017_ownerabout'),
    ]

    operations = [
        migrations.AddField(
            model_name='ownerabout',
            name='owner_about_image',
            field=models.ImageField(default=True, upload_to='AboutImg'),
            preserve_default=False,
        ),
    ]