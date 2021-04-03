from django.db import models
from apps.student.models import *
from apps.teacher.models import *
from apps.courses.models import *
# Create your models here.


class Teacher(models.Model):
    name = models.CharField('Nome', max_length=100)
    cpf = models.CharField('CPF', unique=True, max_length=11)
    address = models.CharField('Endereço', max_length=150)
    salary = models.DecimalField(
        'Remuneração', max_digits=10, decimal_places=2)
    title = models.CharField('Título Docente', max_length=150)
    research = models.CharField('Area de Pesquisa', max_length=150)

    def __str__(self):
        return f'{self.name} - {self.title}'

    class Meta:
        ordering = ['name']
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'
