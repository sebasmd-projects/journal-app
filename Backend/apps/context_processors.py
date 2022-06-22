from .home.models import LogoModel
from .authentication.users.models import PeopleModel
from django.conf import settings


def apps_processors(request):
    ctx = {}

    # Contextos que no dependen de la base de datos
    ctx['url_base'] = settings.BASE_URL

    # Contextos que dependen de la base de datos
    logos = LogoModel.objects.all()
    usuarios = PeopleModel.objects.filter(
        user=request.user.id
    )

    # Obtención de los datos de los contextos
    for logo in logos:
        ctx["logo_light"] = logo.logo_light.url
        ctx["logo_dark"] = logo.logo_dark.url
        ctx["favicon"] = logo.favicon.url

    for usuario in usuarios:
        ctx["full_name"] = usuario.full_name
        ctx["role"] = usuario.get_role_display()

    return ctx
