from django.contrib import admin
from apps.student.models import *
from apps.teacher.models import *
from apps.courses.models import *
# Register your models here.


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'duration']
    search_fields = ['name', 'duration']
