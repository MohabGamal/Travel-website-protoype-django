# Generated by Django 3.1.1 on 2020-10-15 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0020_auto_20201015_1417'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='reply_to_reply',
        ),
    ]
