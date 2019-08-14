import random

from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from django.template import loader
from fuzzywuzzy import fuzz
from panel.models import Image, Letter, Lore, Song

all_searchable_objects = [Image, Letter, Lore, Song]

def jaccard(a, b):
  return float(len(a.intersection(b))) / len(a.union(b))

def score(name, keyword):
  # Fucking nailed it.
  # We score based on two critieria:
  # 1. The fuzzy finding partial_ratio -- This is based on Levenshtein distance
  #      from the input keyword to the target movie title.  I.e. how many steps
  #      it takes to get from one to the other.  However, this by itself
  #      is not sufficient, as 'The Rings' is a perfect partial of a movie
  #      like 'The Lord of the Rings'.  The partial ratio is a number from
  #      0-100.
  # 2. Jaccard Coefficient of the character set.  We take the set of characters
  #      in the keyword and the movie title and take the length of their
  #      intersection divided by the length of their union.  This helps
  #      filter out only partially matching strings.  This returns a number
  #      from 0-1, we scale up to half the max value of the partial_ratio.
  keyword_l = keyword.lower()
  return fuzz.partial_ratio(name, keyword_l) + 50 * jaccard(set(keyword_l), set(name))

def auto_complete(request):
  keyword = request.GET["keyword"]
  data = []
  if keyword:
    data = [x for z in all_searchable_objects for x in z.objects.all()]
    data = sorted(data, key=lambda item: score(item.name.lower(), keyword), reverse = True)
    print(data)
  return JsonResponse(serializers.serialize("json", data[:5]), safe=False)

def songs(request):
  songs = Song.objects.order_by("name")
  return render(request, "songs.html", {"songs": songs})

def controls(request):
  images = Image.objects.order_by("name")
  letters = Letter.objects.order_by("name")
  lores = Lore.objects.order_by("name")
  songs = Song.objects.order_by("name")
  no_cache = random.randint(1, 10000000000)
  return render(request, "controls.html", {
    "images": images,
    "letters": letters,
    "lores": lores,
    "songs": songs,
    "no_cache": random.randint(1, 100000000)
  })

def client(request):
  return render(request, "client.html", {
    "no_cache": random.randint(1, 100000000)
  })
