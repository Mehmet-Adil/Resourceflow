from django.contrib import admin
from .models import User, Student, Teacher, Admin, School

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Admin)
admin.site.register(School)
