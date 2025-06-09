from django.http import JsonResponse
from meteofrance_api import MeteoFranceClient


def search(request):
    q = request.GET.get("q", None)
    client = MeteoFranceClient()
    places = client.search_places(q)
    places_list = [place.__dict__["raw_data"] for place in places]
    return JsonResponse(places_list, safe=False)


def city_forecast(request, slug, lat, lon):
    client = MeteoFranceClient()
    forecast = client.get_forecast(lat, lon).daily_forecast
    return JsonResponse(forecast, safe=False)
