from django.urls import path
from .views import ClassView

app_name = 'settings'
urlpatterns = [
    path('<int:class_id>', ClassView.as_view(), name='class')
]
