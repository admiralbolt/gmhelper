from django.urls import path

from panel import views

urlpatterns = [
    path("songs", views.songs)
]
