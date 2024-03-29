# Generated by Django 4.2.6 on 2023-11-04 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_song'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='song_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='chat.song'),
        ),
        migrations.CreateModel(
            name='MessageAttachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='chat.messages')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.song')),
            ],
        ),
    ]
