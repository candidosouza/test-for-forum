from django.db import models

# Create your models here.


class Setor(models.Model):
    nome = models.CharField('Nome do Setor', max_length=100)

    class Meta:
        verbose_name_plural = 'Setores'

    def __str__(self):
        return self.nome


class SubSetor(models.Model):
    nome = models.CharField('Nome do SubSetor', max_length=100)
    setor = models.ForeignKey(Setor, related_name='subsetor')

    class Meta:
        verbose_name_plural = 'Sub-Setores'

    def __str__(self):
        return self.nome


class Localizacao(models.Model):
    setor = models.ForeignKey(Setor, related_name='setor_localizacao')
    subsetor = models.ForeignKey(SubSetor, related_name='subsetor_localizacao')
    nome = models.CharField('Localização', max_length=100)

    class Meta:
        verbose_name_plural = 'Localizações'

    def __str__(self):
        return self.nome

