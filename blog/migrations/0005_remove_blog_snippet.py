# Generated by Django 3.1.7 on 2021-03-29 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blog_snippet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='snippet',
        ),
    ]
