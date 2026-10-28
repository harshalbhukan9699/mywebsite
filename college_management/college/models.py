from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=20, unique=True)
    duration_years = models.PositiveSmallIntegerField(default=3, verbose_name="Duration (years)")
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.code})"


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=20, unique=True, verbose_name="Roll number")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="students")
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ["course__name", "roll_no"]

    def __str__(self):
        return f"{self.name} - {self.roll_no}"


class Staff(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=80)
    department = models.CharField(max_length=80)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=15, blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "staff"

    def __str__(self):
        return f"{self.name} ({self.designation})"
