from django.db import models
import uuid
from . import *

class Organization(models.Model):
    organization_id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False)
    organization_created = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    organization_modified = models.DateTimeField(null=False, auto_now=True)
    organization_name = models.CharField(max_length=100)
    organization_status =  models.BooleanField()