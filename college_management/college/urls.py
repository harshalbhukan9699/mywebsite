from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("student/", views.student_page, name="student"),
    path("staff/", views.staff_page, name="staff"),
    path("course/", views.course_page, name="course"),
]
