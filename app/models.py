from django.db import models

class Club(models.Model):
    name = models.CharField(max_length=200, unique=True, null=False)
    country = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=True)

    FormationTypes = models.TextChoices('FormationTypes', '4-3-3 4-4-2 4-2-3-1 3-5-2 3-4-3')
    formation = models.CharField(choices = FormationTypes.choices, max_length=10, default='4-3-3', null=False)
    # formation = models.CharField(max_length=10)

    # finances
    total_budget = models.FloatField(default=2e7)
    salary_budget = models.FloatField(default=5e5)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Club'
        verbose_name_plural = 'Clubs'
        ordering =  ['name']

class Player(models.Model):
    name = models.CharField(max_length=200, null=False)
    nationality = models.CharField(max_length=200, null=False)
    birth_year = models.CharField(max_length=4, null=False)
    # overall = models.IntegerField('Média', blank=False)

    PositionTypes = models.TextChoices('PositionTypes', 'GK RB CB LB DM CM RM LM AM SS RW CF LF')
    position = models.CharField(choices=PositionTypes.choices, max_length=2, null=False)  
    
    # matches = models.IntegerField('Partidas', default=0)  
    # goals = models.IntegerField('Gols', default=0)  
    # assists = models.IntegerField('Assistencias', default=0)

    # Dinheiro
    # market_value = models.FloatField('Valor de mercado', default=10_000.00)
    # salary = models.FloatField('Salário', default=5_000.00)

    # Physical 
    height = models.FloatField(default=1.70, null=False)
    weight = models.FloatField(default=70.00, null=False)
    
    # Foot
    FootTypes = models.TextChoices('FootTypes', 'R L')
    foot = models.CharField(choices=FootTypes.choices, max_length=1, default='R', null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    current_club = models.ForeignKey(Club, verbose_name='current club', on_delete=models.CASCADE, related_name='players', null=True) 

    # objects = PlayerManager()

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name = 'Player'
        verbose_name_plural = 'Players'
        ordering =  ['name', 'birth_year']
