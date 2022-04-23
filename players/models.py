from django.db import models

class PlayerManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name_icontains=query) | \
            models.Q(position_icontains=query) | \
            models.Q(nationality_icontains=query)
        )

class Player(models.Model):
    name = models.CharField('Nome', max_length=200, blank=False)
    nationality = models.CharField('Nacionalidade', max_length=150, blank=False)
    age = models.IntegerField('Idade')
    overall = models.IntegerField('Média')
    # Isso vai vir como uma foreign key depois eu adiciono current_club 
    position = models.CharField('Posição', max_length=30)
    ''' Os valores abaixo fazem referencia ao total e nao a temporada '''
    matches = models.IntegerField('Partidas')  
    goals = models.IntegerField('Gols')
    assists = models.IntegerField('Assistencias')

    objects = PlayerManager()

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name = 'Jogador'
        verbose_name_plural = 'Jogadores'
        ordering =  ['overall', 'name']