# Generated by Django 4.2.1 on 2023-05-26 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='cover_song',
        ),
    ]
