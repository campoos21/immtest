# Generated by Django 3.1.2 on 2023-03-22 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('channels', '0002_auto_20230321_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='childs',
            field=models.ManyToManyField(null=True, related_name='_channel_childs_+', to='channels.Channel'),
        ),
    ]
