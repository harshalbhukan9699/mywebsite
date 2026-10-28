import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True
    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100, unique=True)),
                ("code", models.CharField(max_length=20, unique=True)),
                ("duration_years", models.PositiveSmallIntegerField(default=3, verbose_name="Duration (years)")),
                ("description", models.TextField(blank=True)),
            ],
            options={"ordering": ["name"]},
        ),
        migrations.CreateModel(
            name="Staff",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
                ("designation", models.CharField(max_length=80)),
                ("department", models.CharField(max_length=80)),
                ("email", models.EmailField(blank=True, max_length=254)),
                ("phone", models.CharField(blank=True, max_length=15)),
            ],
            options={"verbose_name_plural": "staff", "ordering": ["name"]},
        ),
        migrations.CreateModel(
            name="Student",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
                ("roll_no", models.CharField(max_length=20, unique=True, verbose_name="Roll number")),
                ("email", models.EmailField(blank=True, max_length=254)),
                ("phone", models.CharField(blank=True, max_length=15)),
                ("address", models.CharField(blank=True, max_length=200)),
                ("course", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="students", to="college.course")),
            ],
            options={"ordering": ["course__name", "roll_no"]},
        ),
    ]
