# Generated by Django 3.1.1 on 2020-10-19 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0023_auto_20201019_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]