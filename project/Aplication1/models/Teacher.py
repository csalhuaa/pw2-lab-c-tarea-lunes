from django.db import models
import UUIDfied

from . import *

class Teacher(models.Model):
    teacher_id = models.UUIDfied(
        primary_key = True,
        default = uuid.uuid4,
        editable = False
    )
    organization_id =  models.ForeignKey(Organization, on_delete = models.CASCADE)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    teacher_created = models.DataTimeField(editable= False, null= False)
    teacher_modified= models.DataTimeField(editable= True, null=False, auto_now=True)
    teacher_name = models.CharField(max_length=100)
    teacher_status = models.BooleanField()
    teacher_email = models.EmailField()