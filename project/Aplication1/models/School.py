from django.db import models
import uuid
from .Organization import Organization

class School(models.Model):
    School_id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False)
    organization_id = models.ForeignKey(Organization, on_delete=models.CASCADE)
    school_created = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    school_modified = models.DateTimeField(null=False, auto_now=True)
    school_name = models.CharField(max_length=100)
    school_status =  models.BooleanField()