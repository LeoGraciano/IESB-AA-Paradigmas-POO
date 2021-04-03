from django.contrib import admin
from apps.student.models import *
from apps.teacher.models import *
from apps.courses.models import *
# Register your models here.


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'cpf']
    search_fields = ['id', 'name', 'cpf']
