# Generated by Django 3.2.15 on 2022-09-19 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20220919_1156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user_since',
        ),
    ]