# Generated by Django 4.0.4 on 2023-06-11 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0005_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='news_short_title',
            field=models.CharField(default='<django.db...', max_length=200),
        ),
    ]