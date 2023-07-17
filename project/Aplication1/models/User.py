from django.db import models
import uuid
from .User_Type import User_Type

class User(models.Model):
    user_id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False)
    user_type_id = models.ForeignKey(User_Type, on_delete=models.CASCADE)
    user_dni = models.IntegerField()
    user_dob = models.DateField()
    user_email = models.EmailField()
    user_last_name = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    user_password = models.CharField(max_length=255)