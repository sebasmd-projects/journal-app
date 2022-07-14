from apps.home.models import (
    LogoModel,
    NameAndLinkModel
)

from apps.authentication.users.models import (
    UsersModel,
    PeopleModel
)


from django.conf import settings


def apps_processors(request):
    ctx = {}

    ctx['url_base'] = settings.BASE_URL

    logos = LogoModel.objects.all()
    people = PeopleModel.objects.all()
    users = UsersModel.objects.all()

    ctx["social_network"] = NameAndLinkModel.objects.all()

    for u in users:
        ctx['user_email'] = u.email
        ctx['user_username'] = u.username

    for l in logos:
        ctx["logo_light"] = l.logo_light.url
        ctx["logo_dark"] = l.logo_dark.url
        ctx["favicon"] = l.favicon.url

    for p in people:
        ctx["full_name"] = p.full_name
        ctx["role"] = p.get_role_display()
        ctx["profile_picture"] = p.avatar

    return ctx
