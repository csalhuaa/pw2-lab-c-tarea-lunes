from django.db import models
import uuid
from .Organization import Organization

class Faculty(models.Model):
    faculty_id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False)
    organization_id = models.ForeignKey(Organization, on_delete=models.CASCADE)
    faculty_created = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    faculty_modified = models.DateTimeField(null=False, auto_now=True)
    faculty_name = models.CharField(max_length=100)
    faculty_status =  models.BooleanField()