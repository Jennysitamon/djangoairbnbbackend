# Generated by Django 5.0.2 on 2025-03-27 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conversationmessage',
            old_name='send_to',
            new_name='sent_to',
        ),
    ]
