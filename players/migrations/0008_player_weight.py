# Generated by Django 2.2 on 2022-06-15 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0007_auto_20220615_0849'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='weight',
            field=models.FloatField(default=70.0, verbose_name='Peso'),
        ),
    ]