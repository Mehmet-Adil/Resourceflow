from django.db import models
from django.contrib.auth.models import AbstractUser


class School(models.Model):
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Admin(models.Model):
    admin_user = models.ForeignKey('User', blank=False, null=False, on_delete=models.CASCADE, related_name='admin_user')
    school = models.ForeignKey('School', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.admin_user.username} of {self.school}'


class Teacher(models.Model):
    teacher_user = models.ForeignKey('User', blank=False, null=False, on_delete=models.CASCADE, related_name='teacher_user')
    school = models.ForeignKey('School', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.teacher_user.username} of {self.school}'


class Student(models.Model):
    student_user = models.ForeignKey('User', blank=False, null=False, on_delete=models.CASCADE, related_name='student_user')
    school = models.ForeignKey('School', on_delete=models.CASCADE)

    mother_first_name = models.CharField(max_length=100, null=True, blank=True, default=True)
    mother_last_name = models.CharField(max_length=100, null=True, blank=True, default=True)

    father_first_name = models.CharField(max_length=100, null=True, blank=True, default=True)
    father_last_name = models.CharField(max_length=100, null=True, blank=True, default=True)

    grade = models.ForeignKey('classes.Grade', blank=False, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.student_user.username} of grade: {self.grade.get_full_name()}, in school {self.school.name}'


class User(AbstractUser):
    date_of_birth = models.DateField(max_length=128, blank=True, null=True, default=None)
    admin = models.OneToOneField('Admin', null=True, blank=True, on_delete=models.CASCADE)
    teacher = models.OneToOneField('Teacher', null=True, blank=True, on_delete=models.CASCADE)
    student = models.OneToOneField('Student', null=True, blank=True, on_delete=models.CASCADE)

    def get_rank(self):
        if self.is_superuser:
            return 'Owner'
        elif self.admin:
            return f'Admin of {self.admin.school}'
        elif self.teacher:
            return f'Teacher of {self.teacher.school}'
        elif self.student:
            return f'Student in grade: {self.student.grade}, in {self.student.school}'

    def __str__(self):
        return f'{self.username} - {self.get_rank()}'
