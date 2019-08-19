from django.urls import path
from panel import session
from panel import views

urlpatterns = [
    path("auto_complete", views.auto_complete),
    path("client", views.client),
    path("controls", views.controls),
    path("info_card", views.info_card),
    path("songs", views.songs),
    path("update_session", session.update)
]
