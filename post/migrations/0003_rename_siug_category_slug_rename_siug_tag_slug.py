# Generated by Django 4.2.4 on 2023-08-17 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_alter_post_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='siug',
            new_name='slug',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='siug',
            new_name='slug',
        ),
    ]