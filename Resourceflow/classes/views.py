from django.urls import reverse_lazy
from utils.role_views import RoleControlView


class ClassView(RoleControlView):
    login_url = reverse_lazy('welcome:welcome')
    student_template_name = 'classes/class_student.html'
    teacher_template_name = 'classes/class_teacher.html'
    admin_template_name = 'classes/class_admin.html'
    owner_template_name = 'classes/class_owner.html'
