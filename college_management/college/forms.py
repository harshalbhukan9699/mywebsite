from django import forms
from .models import Course, Student, Staff


class StyledModelForm(forms.ModelForm):
    """Adds the CSS class used by the stylesheet to every field."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.setdefault("class", "field")


class CourseForm(StyledModelForm):
    class Meta:
        model = Course
        fields = ["name", "code", "duration_years", "description"]
        widgets = {"description": forms.Textarea(attrs={"rows": 3})}


class StudentForm(StyledModelForm):
    class Meta:
        model = Student
        fields = ["course", "name", "roll_no", "email", "phone", "address"]


class StaffForm(StyledModelForm):
    class Meta:
        model = Staff
        fields = ["name", "designation", "department", "email", "phone"]
