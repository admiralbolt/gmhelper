from django.shortcuts import render
from django.template import loader

from panel.models import Letter, Lore, Song
import random


def songs(request):
  songs = Song.objects.order_by("name")
  return render(request, "songs.html", {"songs": songs})

def controls(request):
  letters = Letter.objects.order_by("name")
  lores = Lore.objects.order_by("name")
  songs = Song.objects.order_by("name")
  no_cache = random.randint(1, 10000000000)
  return render(request, "controls.html", {
    "letters": letters,
    "lores": lores,
    "songs": songs,
    "no_cache": random.randint(1, 100000000)
  })

def client(request):
  return render(request, "client.html", {
    "no_cache": random.randint(1, 100000000)
  })
