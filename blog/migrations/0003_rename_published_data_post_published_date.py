# Generated by Django 3.2.9 on 2021-11-26 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_auther_post_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='published_data',
            new_name='published_date',
        ),
    ]
