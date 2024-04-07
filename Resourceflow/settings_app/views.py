from django.urls import reverse_lazy
from utils.role_views import RoleControlView


class SettingsView(RoleControlView):
    login_url = reverse_lazy('welcome:welcome')
    student_template_name = 'settings_app/settings_student.html'
    teacher_template_name = 'settings_app/settings_teacher.html'
    admin_template_name = 'settings_app/settings_admin.html'
    owner_template_name = 'settings_app/settings_owner.html'
