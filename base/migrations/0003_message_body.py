# Generated by Django 5.0.1 on 2024-02-14 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_topic_room_host_message_room_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='body',
            field=models.TextField(default=''),
        ),
    ]