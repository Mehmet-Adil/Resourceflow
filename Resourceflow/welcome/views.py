from django.shortcuts import render, redirect, reverse
from django.views import View
from django.conf import settings
from django.core.mail import send_mail


class WelcomeView(View):
    template_name = 'welcome/index.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        if 'SUBMIT' in request.POST:
            subject = 'TEST Resourceflow MAIL SYSTEM!'
            message = f'Hi, this is a test email! We will send emails to schools!'
            recipient_list = [request.POST['RECIPIENT']]
            email_from = settings.EMAIL_HOST_USER
            send_mail(subject, message, email_from, recipient_list)

            return redirect(reverse('welcome:welcome'))

        return render(request, self.template_name)
