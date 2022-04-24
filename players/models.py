from django.db import models

class PlayerManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name_icontains=query) | \
            models.Q(position_icontains=query) | \
            models.Q(nationality_icontains=query)
        )

class Club(models.Model):
    name = models.CharField('Nome', max_length=200, blank=False)
    country = models.CharField('País', max_length=200, blank=False)
    state = models.CharField('Estado', max_length=200, blank=True)
    coeff = models.IntegerField('Coeficiente')
    formation = models.CharField('Formação', max_length=10)

    created_at = models.DateTimeField(
        'Criado em', auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Atualizado em', auto_now=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Clube'
        verbose_name_plural = 'Clubes'
        ordering =  ['coeff', 'name']


class Player(models.Model):
    name = models.CharField('Nome', max_length=200, blank=False)
    nationality = models.CharField('Nacionalidade', max_length=150, blank=False)
    age = models.IntegerField('Idade', blank=False)
    overall = models.IntegerField('Média', blank=False)
    current_club = models.ForeignKey(Club, verbose_name='Clube Atual', blank=True, on_delete=models.CASCADE) 
    position = models.CharField('Posição', max_length=30, blank=False)  
    
    ''' Os valores abaixo fazem referencia ao total e nao a temporada '''
    matches = models.IntegerField('Partidas', default=0)  
    goals = models.IntegerField('Gols', default=0)  
    assists = models.IntegerField('Assistencias', default=0)

    created_at = models.DateTimeField(
        'Criado em', auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Atualizado em', auto_now=True
    )

    objects = PlayerManager()

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name = 'Jogador'
        verbose_name_plural = 'Jogadores'
        ordering =  ['overall', 'name']
