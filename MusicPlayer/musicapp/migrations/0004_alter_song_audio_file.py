# Generated by Django 4.2.7 on 2023-11-27 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0003_alter_song_audio_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='audio_file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
