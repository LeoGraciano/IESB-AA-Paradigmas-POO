from django.db import models
from apps.student.models import *
from apps.teacher.models import *
from apps.courses.models import *
# Create your models here.


class Course(models.Model):
    name = models.CharField('Nome', max_length=100)
    duration = models.PositiveSmallIntegerField('Duração')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name', 'duration']
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
