from django.db import models
import uuid
from .Assignment import Assignment
from .Organization import Organization 
from .Teacher import Teacher 

class Group(models.Model):
    group_id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False
    )
    assignment_id = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    organization_id = models.ForeignKey(Organization, on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    group_created = models.DateTimeField()
    group_modified = models.DateTimeField()
    group_name = models.CharField(max_length=255)
    group_status = models.BooleanField()
