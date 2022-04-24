# Generated by Django 2.2 on 2022-04-24 01:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 4, 24, 1, 9, 8, 492360, tzinfo=utc), verbose_name='Criado em'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Atualizado em'),
        ),
    ]
