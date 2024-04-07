from django.contrib import admin
from .models import Class, Grade, Topic, Post

admin.site.register(Grade)
admin.site.register(Class)
admin.site.register(Topic)
admin.site.register(Post)
