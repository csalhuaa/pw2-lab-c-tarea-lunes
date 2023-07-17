from django.db import models
import uuid
from .Organization import Organization 

class Course(models.Model):
    course_id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False)
    organization_id = models.ForeignKey(Organization, on_delete=models.CASCADE)
    course_created = models.DateTimeField()
    course_modified = models.DateTimeField()
    course_name = models.CharField(max_length=255)
    course_status = models.BooleanField()