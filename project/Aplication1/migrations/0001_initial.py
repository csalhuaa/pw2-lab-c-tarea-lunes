# Generated by Django 4.2.3 on 2023-07-17 17:44

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Academic",
            fields=[
                (
                    "academic_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("academic_created", models.DateTimeField()),
                ("academic_modified", models.DateTimeField()),
                ("academic_name", models.CharField(max_length=255)),
                ("academic_status", models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name="Assignment",
            fields=[
                (
                    "assignment_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("assignment_created", models.DateTimeField()),
                ("assignment_modified", models.DateTimeField()),
                ("assignment_status", models.BooleanField()),
                (
                    "academic_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Aplication1.academic",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Organization",
            fields=[
                (
                    "organization_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("organization_created", models.DateTimeField(auto_now_add=True)),
                ("organization_modified", models.DateTimeField(auto_now=True)),
                ("organization_name", models.CharField(max_length=100)),
                ("organization_status", models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name="School",
            fields=[
                (
                    "School_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("school_created", models.DateTimeField(auto_now_add=True)),
                ("school_modified", models.DateTimeField(auto_now=True)),
                ("school_name", models.CharField(max_length=100)),
                ("school_status", models.BooleanField()),
                (
                    "organization_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Aplication1.organization",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="User_Type",
            fields=[
                (
                    "user_type_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("user_type_created", models.DateTimeField(auto_now_add=True)),
                ("user_type_modified", models.DateTimeField(auto_now=True)),
                ("user_type_name", models.CharField(max_length=100)),
                ("user_type_status", models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "user_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("user_dni", models.IntegerField()),
                ("user_dob", models.DateField()),
                ("user_email", models.EmailField(max_length=254)),
                ("user_last_name", models.CharField(max_length=255)),
                ("user_name", models.CharField(max_length=255)),
                ("user_password", models.CharField(max_length=255)),
                (
                    "user_type_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Aplication1.user_type",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Teacher",
            fields=[
                (
                    "teacher_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("teacher_created", models.DateTimeField(editable=False)),
                ("teacher_modified", models.DateTimeField(auto_now=True)),
                ("teacher_name", models.CharField(max_length=100)),
                ("teacher_status", models.BooleanField()),
                ("teacher_email", models.EmailField(max_length=254)),
                (
                    "organization_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Aplication1.organization",
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Aplication1.user",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "student_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("student_created", models.DateTimeField()),
                ("student_modified", models.DateTimeField()),
                ("student_status", models.BooleanField()),
                (
                    "organization_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Aplication1.organization",
                    ),
                ),
                (
                    "school_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Aplication1.school",
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Aplication1.user",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Semester",
            fields=[
                (
                    "semester_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("semester_created", models.DateTimeField(auto_now_add=True)),
                ("semester_modified", models.DateTimeField(auto_now=True)),
                ("semester_name", models.CharField(max_length=100)),
                ("semester_status", models.BooleanField()),
                (
                    "organization_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Aplication1.organization",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Plan",
            fields=[
                (
                    "plan_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("plan_created", models.DateTimeField(auto_now_add=True)),
                ("plan_modified", models.DateTimeField(auto_now=True)),
                ("plan_name", models.CharField(max_length=100)),
                ("plan_status", models.BooleanField()),
                (
                    "organization_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Aplication1.organization",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Group",
            fields=[
                (
                    "group_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("group_created", models.DateTimeField()),
                ("group_modified", models.DateTimeField()),
                ("group_name", models.CharField(max_length=255)),
                ("group_status", models.BooleanField()),
                (
                    "assignment_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Aplication1.assignment",
                    ),
                ),
                (
                    "organization_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Aplication1.organization",
                    ),
                ),
                (
                    "teacher_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Aplication1.teacher",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Faculty",
            fields=[
                (
                    "faculty_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("faculty_created", models.DateTimeField(auto_now_add=True)),
                ("faculty_modified", models.DateTimeField(auto_now=True)),
                ("faculty_name", models.CharField(max_length=100)),
                ("faculty_status", models.BooleanField()),
                (
                    "organization_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Aplication1.organization",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Enroll",
            fields=[
                (
                    "enroll_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("enroll_created", models.DateTimeField()),
                ("enroll_modified", models.DateTimeField()),
                ("enroll_status", models.BooleanField()),
                (
                    "group_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Aplication1.group",
                    ),
                ),
                (
                    "organization_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Aplication1.organization",
                    ),
                ),
                (
                    "student_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Aplication1.student",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Department",
            fields=[
                (
                    "department_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("department_created", models.DateTimeField()),
                ("department_modified", models.DateTimeField()),
                ("department_name", models.CharField(max_length=255)),
                ("department_status", models.BooleanField()),
                (
                    "organization_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Aplication1.organization",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "course_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("course_created", models.DateTimeField()),
                ("course_modified", models.DateTimeField()),
                ("course_name", models.CharField(max_length=255)),
                ("course_status", models.BooleanField()),
                (
                    "organization_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Aplication1.organization",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="assignment",
            name="course_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="Aplication1.course"
            ),
        ),
        migrations.AddField(
            model_name="assignment",
            name="organization_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="Aplication1.organization",
            ),
        ),
        migrations.AddField(
            model_name="assignment",
            name="teacher_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="Aplication1.teacher"
            ),
        ),
        migrations.AddField(
            model_name="academic",
            name="department_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="Aplication1.department"
            ),
        ),
        migrations.AddField(
            model_name="academic",
            name="organization_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="Aplication1.organization",
            ),
        ),
    ]
