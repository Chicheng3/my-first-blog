# Generated by Django 3.2.9 on 2021-11-26 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_published_data_post_published_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='created_data',
            new_name='created_date',
        ),
    ]
