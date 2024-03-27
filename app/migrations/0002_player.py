# Generated by Django 4.0.5 on 2024-03-27 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('nationality', models.CharField(max_length=200)),
                ('birth_year', models.CharField(max_length=4)),
                ('position', models.CharField(choices=[('GK', 'Gk'), ('RB', 'Rb'), ('CB', 'Cb'), ('LB', 'Lb'), ('DM', 'Dm'), ('CM', 'Cm'), ('RM', 'Rm'), ('LM', 'Lm'), ('AM', 'Am'), ('SS', 'Ss'), ('RW', 'Rw'), ('CF', 'Cf'), ('LF', 'Lf')], max_length=2)),
                ('height', models.FloatField(default=1.7)),
                ('weight', models.FloatField(default=70.0)),
                ('foot', models.CharField(choices=[('R', 'R'), ('L', 'L')], default='R', max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('current_club', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='players', to='app.club', verbose_name='current club')),
            ],
            options={
                'verbose_name': 'Player',
                'verbose_name_plural': 'Players',
                'ordering': ['name', 'birth_year'],
            },
        ),
    ]