from django.urls import reverse_lazy

from django.db.models import Q

from django.views.generic import TemplateView

from django.views.generic.edit import FormView

from apps.authentication.users.models import PeopleModel, UsersModel

from apps.journal.general_app.forms import ManagementPeopleEditForm, ManagementPeopleAvatarForm

DASHBOARD_TEMPLATE_PATH = "journal/general_app/templates/dashboards/index.html"
USAGE_TEMPLATE_PATH = "journal/general_app/templates/documentation/usage.html"
COMPONENTS_TEMPLATE_PATH = "journal/general_app/templates/documentation/components.html"
CHANGELOG_TEMPLATE_PATH = "journal/general_app/templates/documentation/changelog.html"
USERMANAGEMENTEDIT_TEMPLATE_PATH = "journal/general_app/templates/user_management/edit.html"
USERMANAGEMENTAVATAR_TEMPLATE_PATH = "journal/general_app/templates/user_management/avatar.html"


class ManagementPeopleEditFormView(FormView):
    template_name = USERMANAGEMENTEDIT_TEMPLATE_PATH
    form_class = ManagementPeopleEditForm

    def get_context_data(self, **kwargs):
        context = super(ManagementPeopleEditFormView,
                        self).get_context_data(**kwargs)

        context['avatar'] = PeopleModel.objects.get(
            id=self.kwargs['pk']
        ).avatar

        return context

    def get_initial(self):

        initial = super(ManagementPeopleEditFormView, self).get_initial()

        initial['first_name'] = PeopleModel.objects.get(
            id=self.kwargs['pk']
        ).first_name

        initial['last_name'] = PeopleModel.objects.get(
            id=self.kwargs['pk']
        ).last_name

        initial['phone'] = PeopleModel.objects.get(
            id=self.kwargs['pk']
        ).phone

        initial['gender'] = PeopleModel.objects.get(
            id=self.kwargs['pk']
        ).gender

        initial['email'] = UsersModel.objects.get(
            id=self.kwargs['pk']
        ).email

        return initial

    def form_valid(self, form):

        PeopleModel.objects.filter(
            Q(phone=form.cleaned_data['phone']) | Q(id=self.kwargs['pk'])
        ).update(
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            phone=form.cleaned_data['phone'],
            birthday=form.cleaned_data['birthday'],
            gender=form.cleaned_data['gender']
        )

        UsersModel.objects.filter(
            Q(id=self.kwargs['pk']) | Q(email=form.cleaned_data['email'])
        ).update(
            email=form.cleaned_data['email'],
        )

        return super(ManagementPeopleEditFormView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            'journal_general:edit-avatar',
            kwargs={'pk': self.kwargs['pk']}
        )


class ManagementPeopleAvatarFormView(FormView):
    template_name = USERMANAGEMENTAVATAR_TEMPLATE_PATH
    form_class = ManagementPeopleAvatarForm

    def form_valid(self, form):

        PeopleModel.objects.filter(
            id=self.kwargs['pk']
        ).update(
            avatar=form.cleaned_data['avatar'],
        )

        return super(ManagementPeopleAvatarFormView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            'journal_general:edit-avatar',
            kwargs={'pk': self.kwargs['pk']}
        )


class DashBoardTemplateView(TemplateView):
    template_name = DASHBOARD_TEMPLATE_PATH

    def get_context_data(self, **kwargs):
        context = super(DashBoardTemplateView, self).get_context_data(**kwargs)

        return context
