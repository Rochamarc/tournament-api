from tabnanny import verbose
from django.db import models

from clubs.models import Club


class Game(models.Model):

    competition = models.CharField('Competição', max_length=200)
    season = models.CharField('Temporada', max_length=5)
    hour = models.CharField('Horario', max_length=5)
    home_team = models.ForeignKey(Club, verbose_name='Time Anfitrião', related_name='%(class)s_home', on_delete=models.CASCADE)
    away_team = models.ForeignKey(Club, verbose_name='Time Visitante', related_name='%(class)s_away', on_delete=models.CASCADE)
    score = models.CharField('Placar', max_length=10)
    stadium = models.TextField('Estádio')

    home_shots = models.IntegerField('Chutes do Anfitrião', null=False)
    home_shots_on_target = models.IntegerField('Chutes no Alvo Anfitrião', null=False)
    home_fouls = models.IntegerField('Faltas do Anfitrião', null=False) 
    home_tackles = models.IntegerField('Divididas do Anfitrião', null=False)
    home_saves = models.IntegerField('Defesas do Anfitrião', null=False)
    home_ball_possession = models.IntegerField('Posse de Bola do Anfitrião', null=False)
    home_offsides = models.IntegerField('Impedimentos do Anfitrião', null=False)
    home_freekicks = models.IntegerField('Faltas do Anfitrião', null=False)

    away_shots = models.IntegerField('Chutes do Visitante', null=False)
    away_shots_on_target = models.IntegerField('Chutes no Alvo do Visitante', null=False)
    away_fouls = models.IntegerField('Faltas do Visitante', null=False)
    away_tackles = models.IntegerField('Divididas do Visitante', null=False)
    away_saves = models.IntegerField('Defesas do Visitante', null=False)
    away_ball_possession = models.IntegerField('Posse de bola do Visitante', null=False)
    away_offsides = models.IntegerField('Impedimentos do Visitante', null=False)
    away_freekicks = models.IntegerField('Faltas do Visitante', null=False)

    created_at = models.DateTimeField(
        'Criado em', auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Atualizado em', auto_now=True
    )

    def __str__(self):
        return f'{self.home_team} x {self.away_team} :: {self.competition}'

    class Meta:
        verbose_name = 'Jogo'
        verbose_name_plural = 'Jogos'
        ordering =  ['season', 'competition']