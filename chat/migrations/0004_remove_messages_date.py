# Generated by Django 4.2.7 on 2023-11-06 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_messages_date_alter_song_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messages',
            name='date',
        ),
    ]
