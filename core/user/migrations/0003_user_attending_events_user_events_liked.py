# Generated by Django 4.0 on 2023-11-01 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_event', '0004_event_age_limit'),
        ('core_user', '0002_user_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='attending_events',
            field=models.ManyToManyField(related_name='attending_by', to='core_event.Event'),
        ),
        migrations.AddField(
            model_name='user',
            name='events_liked',
            field=models.ManyToManyField(related_name='liked_by', to='core_event.Event'),
        ),
    ]