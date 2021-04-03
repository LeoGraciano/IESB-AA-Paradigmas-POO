from django.db import models
from apps.student.models import *
from apps.teacher.models import *
from apps.courses.models import *
# Create your models here.


class Student_vs_Course(models.Model):
    student = models.OneToOneField(
        Student, verbose_name='Estudante',
        on_delete=models.SET_NULL, null=True
    )

    course = models.ManyToManyField(
        Course, verbose_name='Curso',
    )

    def __str__(self):
        import re
        courses = (Student_vs_Course.objects.get(id=self.id)).course.all()
        courses_list = [course.name for course in courses]
        replace_list = re.sub("['[\]]", "", str(courses_list))
        return f'{self.student} - Cursando: {replace_list.replace(","," e ")}'

    class Meta:
        verbose_name = 'Estudante no Curso'
        verbose_name_plural = 'Estudante nos Cursos'


class Teacher_vs_Course(models.Model):
    teacher = models.OneToOneField(
        Teacher, verbose_name='Professor',
        on_delete=models.SET_NULL, null=True
    )

    course = models.ManyToManyField(
        Course, verbose_name='Cursos'
    )

    def __str__(self):
        import re
        courses = (Teacher_vs_Course.objects.get(id=self.id)).course.all()
        courses_list = [course.name for course in courses]
        replace_list = re.sub("['[\]]", "", str(courses_list))
        return f'{self.teacher} - Disciplinas: {replace_list.replace(","," e ")}'

    class Meta:
        verbose_name = 'Professor do Curso'
        verbose_name_plural = 'Professor dos cursos'
