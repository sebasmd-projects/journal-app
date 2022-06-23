from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from django.views.generic import View


from .forms import (
    UserLoginForm,
    UpdatePasswordForm,
)


class UserLoginView(FormView):
    template_name = "auth/templates/login/login.html"
    form_class = UserLoginForm

    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        login(self.request, user)
        return super(UserLoginView, self).form_valid(form)
    
    def get_success_url(self):
        next_url = self.request.POST.get('next',None)
        
        if next_url:
            return "%s" % (next_url)
        else :
            return reverse('journal_general:dashboard')


class UserLogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'authentication_login:user-login'
            )
        )


class UpdatePassword(LoginRequiredMixin, FormView):
    template_name = "auth/templates/change-password/change-password.html"
    form_class = UpdatePasswordForm
    success_url = reverse_lazy('authentication_login:user-login')
    login_url = reverse_lazy('authentication_login:user-login')

    def form_valid(self, form):
        usr = self.request.user
        user = authenticate(
            username=usr.username,
            password=form.cleaned_data['password']
        )

        if user:
            new_password = form.cleaned_data['new_password']
            usr.set_password(new_password)

        logout(self.request)
        return super(UpdatePassword, self).form_valid(form)
