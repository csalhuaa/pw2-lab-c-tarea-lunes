from django.db import models
import uuid
from .Organization import Organization
from .School import School
from .User import User

class Student(models.Model):
    student_id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False
    )
    organization_id = models.ForeignKey(Organization, on_delete=models.CASCADE)
    school_id = models.ForeignKey(School, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    student_created = models.DateTimeField()
    student_modified = models.DateTimeField()
    student_status = models.BooleanField()