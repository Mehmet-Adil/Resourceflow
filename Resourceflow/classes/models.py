from django.db import models


class Grade(models.Model):
    school = models.ForeignKey('account.School', blank=False, null=False, on_delete=models.CASCADE)
    year = models.PositiveSmallIntegerField(blank=False, null=False)
    suffix = models.CharField(max_length=25, blank=False, null=False)
    alias = models.CharField(max_length=100, blank=True, null=True)

    def get_full_name(self):
        return self.alias if self.alias else f'{self.year}{self.suffix}'

    def __str__(self):
        return f'{self.get_full_name()} of {self.school}'


class Class(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    teachers = models.ManyToManyField('account.Teacher')
    students = models.ManyToManyField('account.Student')
    grade = models.ForeignKey('Grade', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Classes'

    def __str__(self):
        return f'{self.name} Class, in {str(self.grade)}'


class Topic(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    of_class = models.ForeignKey('Class', on_delete=models.CASCADE, verbose_name='Class')

    def __str__(self):
        return f'Topic: {self.name}, of Class: {self.of_class}'


class Post(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE)
    author = models.ForeignKey('account.User', blank=False, null=True, on_delete=models.SET_NULL)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Post: {self.title}, of Topic: {self.topic.name}, by Author: {self.author.username}'
