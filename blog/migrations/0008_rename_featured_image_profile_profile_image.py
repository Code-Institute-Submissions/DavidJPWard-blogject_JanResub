# Generated by Django 3.2.15 on 2022-09-18 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_profile_subscribers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='featured_image',
            new_name='profile_image',
        ),
    ]