# Generated by Django 3.2.15 on 2022-09-16 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20220914_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(blank=True, choices=[('Politics', 'Politics'), ('Technology', 'Technology'), ('TV & Film', 'TV & Film'), ('Video Games', 'Video Games'), ('Science', 'Science'), ('Sports', 'Sports'), ('Fashion', 'Fashion'), ('Music', 'Music')], max_length=30, null=True),
        ),
    ]