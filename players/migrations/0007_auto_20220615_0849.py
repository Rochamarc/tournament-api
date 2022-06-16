# Generated by Django 2.2 on 2022-06-15 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0006_auto_20220514_0027'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='average',
            field=models.FloatField(default=0.0, verbose_name='Média'),
        ),
        migrations.AddField(
            model_name='player',
            name='foot',
            field=models.CharField(default='Right', max_length=50, verbose_name='Pé preferido'),
        ),
        migrations.AddField(
            model_name='player',
            name='height',
            field=models.FloatField(default=1.7, verbose_name='Altura'),
        ),
        migrations.AddField(
            model_name='player',
            name='market_value',
            field=models.FloatField(default=10000.0, verbose_name='Valor de mercado'),
        ),
        migrations.AddField(
            model_name='player',
            name='salary',
            field=models.FloatField(default=5000.0, verbose_name='Salário'),
        ),
    ]