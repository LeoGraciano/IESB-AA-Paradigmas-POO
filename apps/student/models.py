from django.db import models
from apps.student.models import *
from apps.teacher.models import *
from apps.courses.models import *
# Create your models here.


class Student(models.Model):
    name = models.CharField('Nome', max_length=100)
    cpf = models.CharField('CPF', unique=True, max_length=11)
    address = models.CharField('Endereço', max_length=150)

    def __str__(self):
        return f'{self.id} - {self.name}'

    class Meta:
        ordering = ['name']
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
