from django.db import models
import uuid

class User_Type(models.Model):
    user_type_id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False)
    user_type_created = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    user_type_modified = models.DateTimeField(null=False, auto_now=True)
    user_type_name = models.CharField(max_length=100)
    user_type_status =  models.BooleanField()