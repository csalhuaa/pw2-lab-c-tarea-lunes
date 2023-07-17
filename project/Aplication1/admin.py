from django.contrib import admin

from .models.Academic import Academic
from .models.Assignment import Assignment
from .models.Course import Course 
from .models.Department import Department 
from .models.Enroll import Enroll 
from .models.Faculty import Faculty 
from .models.Group import Group 
from .models.Organization import Organization 
from .models.Plan import Plan 
from .models.School import School 
from .models.Semester import Semester 
from .models.Student import Student
from .models.User import User
from .models.User_Type import User_Type
from .models.Teacher import Teacher 

# Register your models here.
admin.site.register(Academic)
admin.site.register(Assignment)
admin.site.register(Course)
admin.site.register(Department)
admin.site.register(Enroll)
admin.site.register(Faculty)
admin.site.register(Group)
admin.site.register(Organization)
admin.site.register(Plan)
admin.site.register(School)
admin.site.register(Semester)
admin.site.register(Student)
admin.site.register(User)
admin.site.register(User_Type)
admin.site.register(Teacher)