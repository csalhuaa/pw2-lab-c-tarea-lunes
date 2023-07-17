from django.db import models
import uuid
from .Academic import Academic
from .Course import Course
from .Organization import Organization
from .Teacher import Teacher 

class Assignment(models.Model):
    assignment_id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False)
    academic_id = models.ForeignKey(Academic, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    organization_id = models.ForeignKey(Organization, on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    assignment_created = models.DateTimeField()
    assignment_modified = models.DateTimeField()
    assignment_status = models.BooleanField()