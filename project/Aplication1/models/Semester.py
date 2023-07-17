from django.db import models
import uuid
from .Organization import Organization

class Semester(models.Model):
    semester_id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False)
    organization_id = models.ForeignKey(Organization, on_delete=models.CASCADE)
    semester_created = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    semester_modified = models.DateTimeField(null=False, auto_now=True)
    semester_name = models.CharField(max_length=100)
    semester_status =  models.BooleanField()