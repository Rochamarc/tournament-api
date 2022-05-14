# Generated by Django 2.2 on 2022-05-13 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clubs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nome')),
                ('nationality', models.CharField(max_length=150, verbose_name='Nacionalidade')),
                ('age', models.IntegerField(verbose_name='Idade')),
                ('formation', models.TextField(verbose_name='Formação')),
                ('play_mode', models.TextField(verbose_name='Modo de Jogo')),
                ('current_club', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='clubs.Club', verbose_name='Clube Atual')),
            ],
        ),
    ]
