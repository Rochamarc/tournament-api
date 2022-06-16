from django.db import models

from players.models import Player

class SeasonIndividualPlayerStats(models.Model):
    ''' Essa classse será altamente atualizada '''

    season = models.CharField('Temporada', max_length=5)
    competition = models.CharField('Competição', max_length=100)

    # Foreign key
    player_owner = models.ForeignKey(Player, verbose_name='Jogador', related_name='season_individual_player_stats', on_delete=models.CASCADE)

    # This is not a foreign key because i'm not interest in register the club object
    # it's just a register of in wich club the player was defending on that season
    club = models.CharField('Clube', max_length=200)


    # stats
    goals = models.IntegerField('Gols', default=0)
    assists = models.IntegerField('Assistencias', default=0)
    shots_on_target = models.IntegerField('Chutes no alvo', default=0)
    saves = models.IntegerField('Defesas', default=0)
    hard_saves = models.IntegerField('Defesas dificeis', default=0)
    tackles = models.IntegerField('Disputas ganhas', default=0)

    created_at = models.DateTimeField(
        'Criado em', auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Atualizado em', auto_now=True
    )

    def __str__(self):
        return f"{self.player_owner} {self.competition} {self.season}"
    
    class Meta:
        verbose_name = 'Statistica Individual Por Temporada'
        verbose_name_plural = 'Statisticas Individuais Por Temporada'
        ordering = ['season']