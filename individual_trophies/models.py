from django.db import models

from players.models import Player 

class IndividualTrophy(models.Model):
    season = models.CharField('Temporada', max_length=5)
    competition = models.CharField('Competição', max_length=100)
    category = models.CharField('Categoria', max_length=200)

    # Foreign Key
    player_owner = models.ForeignKey(Player, verbose_name='Vencedor', related_name='individual_trophies', on_delete=models.CASCADE)

    created_at = models.DateTimeField(
        'Criado em', auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Atualizado em', auto_now=True
    )

    def __str__(self):
        return f"{self.competition} {self.season}"

    class Meta:
        verbose_name = 'Prêmio Individual'
        verbose_name_plural = 'Prêmios Individuals'
        ordering = ['competition']