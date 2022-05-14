from django.db import models

from clubs.models import Club 

class Coach(models.Model):
    name = models.CharField('Nome', max_length=200, blank=False)
    nationality = models.CharField('Nacionalidade', max_length=150, blank=False)
    age = models.IntegerField('Idade', blank=False)
    formation = models.TextField('Formação')
    play_mode = models.TextField('Modo de Jogo')

    current_club = models.ForeignKey(Club, verbose_name='Clube Atual', blank=True, on_delete=models.CASCADE, related_name='coach')


    created_at = models.DateTimeField(
        'Criado em', auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Atualizado em', auto_now=True
    )

    def __str__(self):
        return self.name 
        
    class Meta:
        verbose_name = 'Técnico'
        verbose_name_plural = 'Técnicos'
        ordering = ['name']