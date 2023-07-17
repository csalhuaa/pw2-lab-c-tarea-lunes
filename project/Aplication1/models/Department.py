from django.db import models
import uuid
from . import *

class Department(models.Model):
    department_id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False)
    organization_id = models.ForeignKey(Organization, on_delete=models.CASCADE)
    department_created = models.DateTimeField()
    department_modified = models.DateTimeField()
    department_name = models.CharField()
    department_status = models.BooleanField()