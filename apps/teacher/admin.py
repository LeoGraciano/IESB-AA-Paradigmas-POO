from django.contrib import admin
from apps.student.models import *
from apps.teacher.models import *
from apps.courses.models import *
# Register your models here.


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'cpf']
    search_fields = ['name', 'title', 'cpf']
