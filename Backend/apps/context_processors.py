from .home.models import LogoModel

def apps_processors(request):
    ctx = {}
    logos = LogoModel.objects.all()
    for logo in logos:
         ctx["logo_light"] = logo.logo_light.url
         ctx["logo_dark"] = logo.logo_dark.url
         ctx["favicon"] = logo.favicon.url
    return ctx