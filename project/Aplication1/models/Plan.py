from django.db import models
import uuid
from .Organization import Organization

class Plan(models.Model):
    plan_id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False)
    organization_id = models.ForeignKey(Organization, on_delete=models.CASCADE)
    plan_created = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    plan_modified = models.DateTimeField(null=False, auto_now=True)
    plan_name = models.CharField(max_length=100)
    plan_status =  models.BooleanField()