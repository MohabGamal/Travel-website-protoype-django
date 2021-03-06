# Generated by Django 3.1.1 on 2020-10-12 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0015_remove_postviews_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to='comments/'),
        ),
        migrations.AddField(
            model_name='comment',
            name='reply',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='blog_app.comment'),
        ),
    ]
