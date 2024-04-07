# Generated by Django 4.0.5 on 2024-04-07 02:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_seasonindividualplayerstats_competition'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trophy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.CharField(max_length=4)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trophies', to='app.club', verbose_name='champion')),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.competitions', verbose_name='competition')),
            ],
            options={
                'ordering': ['season'],
            },
        ),
    ]
