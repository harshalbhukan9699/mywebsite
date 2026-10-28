from django.contrib import admin
from .models import Course, Staff, Student


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "duration_years")
    search_fields = ("name", "code")


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "roll_no", "course", "phone")
    list_filter = ("course",)
    search_fields = ("name", "roll_no")


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ("name", "designation", "department", "phone")
    list_filter = ("department",)
    search_fields = ("name", "department")
