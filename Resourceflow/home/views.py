from django.urls import reverse_lazy
from utils.role_views import RoleControlView


class HomeView(RoleControlView):
    login_url = reverse_lazy('welcome:welcome')
    student_template_name = 'home/home_student.html'
    teacher_template_name = 'home/home_teacher.html'
    admin_template_name = 'home/home_admin.html'
    owner_template_name = 'home/home_owner.html'
