from django.db import models
import uuid
from .Student import Student
from .Group import Group 
from .Organization import Organization 


class Enroll(models.Model):
    enroll_id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    organization_id = models.ForeignKey(Organization, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    enroll_created = models.DateTimeField()
    enroll_modified = models.DateTimeField()
    enroll_status = models.BooleanField()