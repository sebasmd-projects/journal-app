from django.conf import settings
from django.views.generic.edit import FormView
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.utils import timezone

#
from .forms import (
    UserRegisterForm,
    VerificationCodeForm
)

#
from ..users.models import UsersModel

#
from .functions import generate_random_code


class UserRegisterView(FormView):
    template_name = 'authentication/register/register.html'
    form_class = UserRegisterForm
    success_url = '/'

    def form_valid(self, form):
        v_code = generate_random_code()

        user = UsersModel.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password'],
            privacy=form.cleaned_data['privacy'],
            verification_code=v_code
        )

        send_date = timezone.now

        user_id = user.id

        user_url = f"{settings.BASE_URL[0]}/auth/verificar-usuario/{user_id}/"

        email_text = render_to_string(
            'authentication/register/email/code_verification_email.txt',
            {'code': v_code, 'time': send_date, 'user_url': user_url}
        )

        email_html = render_to_string(
            'authentication/register/email/code_verification_email.html',
            {'code': v_code, 'time': send_date, 'user_url': user_url}
        )
        
        send_mail(
            subject = f'Verifica tu dirección de correo | Journal APP',
            message=email_text,
            from_email = settings.DEFAULT_FROM_EMAIL,
            recipient_list= ['copy_codes@sebasmd.com', form.cleaned_data['email']],
            html_message = email_html,
        )

        return HttpResponseRedirect(
            reverse(
                'authentication_register:user-verification',
                kwargs={'pk': user.id}
            )
        )


class VerificationCodeView(FormView):
    template_name = 'authentication/register/validation-code.html'
    form_class = VerificationCodeForm
    success_url = reverse_lazy('authentication_login:user-login')

    def get_form_kwargs(self):
        kwargs = super(VerificationCodeView, self).get_form_kwargs()
        kwargs.update({
            'pk': self.kwargs['pk'],
        })
        return kwargs

    def form_valid(self, form):

        UsersModel.objects.filter(
            id=self.kwargs['pk']
        ).update(
            is_active=True
        )

        return super(VerificationCodeView, self).form_valid(form)
