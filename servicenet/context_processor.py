from django.conf import settings


def base_context_processors(request):
    return {'GOOGLE_MAPS_API_KEY': settings.GOOGLE_MAPS_API_KEY}
