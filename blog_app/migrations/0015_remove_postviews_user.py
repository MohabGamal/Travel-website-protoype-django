# Generated by Django 3.1.1 on 2020-10-09 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0014_postviews_ipaddres'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postviews',
            name='user',
        ),
    ]
