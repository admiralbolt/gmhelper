from django.urls import path

from panel import views

urlpatterns = [
    path("songs", views.songs),
    path("controls", views.controls),
    path("client", views.client),
]
