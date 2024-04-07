from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class RoleControlView(LoginRequiredMixin, View):
    student_template_name = None
    teacher_template_name = None
    admin_template_name = None
    owner_template_name = None

    def get(self, request, **kwargs):
        if request.user.student:
            return self.get_student(request, **kwargs)
        elif request.user.teacher:
            return self.get_teacher(request, **kwargs)
        elif request.user.admin:
            return self.get_admin(request, **kwargs)
        elif request.user.is_superuser:
            return self.get_owner(request, **kwargs)

    def get_student(self, request, **kwargs):
        return render(request, self.student_template_name, kwargs)

    def get_teacher(self, request, **kwargs):
        return render(request, self.teacher_template_name, kwargs)

    def get_admin(self, request, **kwargs):
        return render(request, self.admin_template_name, kwargs)

    def get_owner(self, request, **kwargs):
        return render(request, self.owner_template_name, kwargs)

    def post(self, request, **kwargs):
        if request.user.is_student:
            return self.post_student(**kwargs)
        elif request.user.is_teacher:
            return self.post_teacher(**kwargs)
        elif request.user.is_admin:
            return self.post_admin(**kwargs)
        elif request.user.is_superuser:
            return self.post_owner(**kwargs)

    def post_student(self, **kwargs):
        return redirect(self.student_template_name, kwargs)

    def post_teacher(self, **kwargs):
        return redirect(self.teacher_template_name, kwargs)

    def post_admin(self, **kwargs):
        return redirect(self.admin_template_name, kwargs)

    def post_owner(self, **kwargs):
        return redirect(self.owner_template_name, kwargs)
