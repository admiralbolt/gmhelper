from django.shortcuts import render
from django.template import loader

from panel.models import Song
import random


no_cache = random.randint(1, 10000000000)

def songs(request):
  songs = Song.objects.order_by("name")
  return render(request, "songs.html", {"songs": songs})

def controls(request):
  return render(request, "controls.html", {"no_cache": no_cache})

def client(request):
  return render(request, "client.html", {"no_cache": no_cache})
