from django.contrib import admin
from .models import Student_vs_Course, Teacher_vs_Course
# Register your models here.


@admin.register(Student_vs_Course)
class Student_vs_CourseAdmin(admin.ModelAdmin):
    search_fields = ['student', 'course']


@admin.register(Teacher_vs_Course)
class Teacher_vs_CourseAdmin(admin.ModelAdmin):
    search_fields = ['teacher', 'course']
