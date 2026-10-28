from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import CourseForm, StaffForm, StudentForm
from .models import Course, Staff, Student


def home(request):
    return render(request, "college/home.html", {
        "counts": {
            "student": Student.objects.count(),
            "staff": Staff.objects.count(),
            "course": Course.objects.count(),
        }
    })


def student_page(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added.")
            return redirect("student")
    else:
        # Pre-select the course when filtering course-wise
        form = StudentForm(initial={"course": request.GET.get("course") or None})

    students = Student.objects.select_related("course")
    selected = request.GET.get("course", "")
    if selected.isdigit():
        students = students.filter(course_id=selected)

    return render(request, "college/student.html", {
        "form": form,
        "students": students,
        "courses": Course.objects.all(),
        "selected": selected,
    })


def staff_page(request):
    if request.method == "POST":
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Staff member added.")
            return redirect("staff")
    else:
        form = StaffForm()
    return render(request, "college/staff.html", {"form": form, "staff_list": Staff.objects.all()})


def course_page(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Course added.")
            return redirect("course")
    else:
        form = CourseForm()
    return render(request, "college/course.html", {"form": form, "courses": Course.objects.all()})
