from django.db import models

from clubs.models import Club

class Table(models.Model):
    season = models.CharField('Temporada', max_length=5)
    competition = models.CharField('Competição', max_length=200)

    club = models.ForeignKey(Club, verbose_name='Clube', on_delete=models.CASCADE, related_name='club')

    points = models.IntegerField('Pontos')
    matches_played = models.IntegerField('Partidas Jogadas')
    won = models.IntegerField('Vitórias')
    draw = models.IntegerField('Empates')
    lost = models.IntegerField('Derrotas')
    goals_for = models.IntegerField('Gols feitos')
    goals_against = models.IntegerField('Gols sofridos') 
    goals_diff = models.IntegerField('Saldo de gols')

    created_at = models.DateTimeField(
        'Criado em', auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Atualizado em', auto_now=True
    )

    def __str__(self):
        return f"{self.club} {self.season}"
