from django.db import models

from clubs.models import Club 

class Trophy(models.Model):
    season = models.CharField('Temporada', max_length=5)
    competition = models.CharField('Competição', max_length=100)

    # Foreign Key
    club_owner = models.ForeignKey(Club, verbose_name='Clube Campeão', related_name='trophies', on_delete=models.CASCADE)

    created_at = models.DateTimeField(
        'Criado em', auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Atualizado em', auto_now=True
    )

    def __str__(self):
        return f"{self.competition} {self.season}"

    class Meta:
        verbose_name = 'Troféu'
        verbose_name_plural = 'Troféus'
        ordering = ['competition']