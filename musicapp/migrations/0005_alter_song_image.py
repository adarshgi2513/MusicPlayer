# Generated by Django 4.2.7 on 2023-11-28 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0004_alter_song_audio_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='image',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
