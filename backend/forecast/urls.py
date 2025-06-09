from django.urls import path

from . import views

urlpatterns = [
    path("search", views.search),
    path("<str:slug>/<str:lat>/<str:lon>/", views.city_forecast),
    # path("", views.index, name="index"),
]
