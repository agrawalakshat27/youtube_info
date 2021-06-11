# Generated by Django 2.2.6 on 2021-06-11 21:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0003_remove_video_thumbernails'),
    ]

    operations = [
        migrations.AddField(
            model_name='thumbernail',
            name='video',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='video.Video'),
            preserve_default=False,
        ),
    ]
