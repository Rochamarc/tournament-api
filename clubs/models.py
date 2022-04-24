from django.db import models


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
