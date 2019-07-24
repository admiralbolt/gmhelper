from django.shortcuts import render
from django.template import loader

from panel.models import Song


def songs(request):
  songs = Song.objects.order_by("name")
  return render(request, "songs.html", {"songs": songs})
