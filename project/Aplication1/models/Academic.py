from django.db import models
import uuid
from .Organization import Organization
from .Department import Department

class Academic(models.Model):
    academic_id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    organization_id = models.ForeignKey(Organization, on_delete=models.CASCADE)
    academic_created = models.DateTimeField()
    academic_modified = models.DateTimeField()
    academic_name = models.CharField(max_length=255)
    academic_status = models.BooleanField()