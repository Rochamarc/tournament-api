# Generated by Django 2.2 on 2022-05-14 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0003_auto_20220514_0027'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coach',
            options={'ordering': ['name'], 'verbose_name': 'Técnico', 'verbose_name_plural': 'Técnicos'},
        ),
    ]