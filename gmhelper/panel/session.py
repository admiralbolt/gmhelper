import random

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from panel.models import Campaign, Image, Letter, Lore, Session, Song

def update(request):
  """Update the currently loaded campaign session.

  This will render a template that has all necessary html for the session
  panel.
  """
  session = Session.objects.get(id=request.GET["key"])
  request.session["session"] = session.pk
  return render(request, "session_panel.html", {
    "session": session,
    "no_cache": random.randint(1, 100000000)
  })

def content(request):
  """Render the current session content."""
  session = Session.objects.get(id=request.session["session"])
  return render(request, "session_content.html", {
    "session": session,
    "no_cache": random.randint(1, 100000000)
  })

@csrf_exempt
def save(request):
  """Save the updated text of the current session.

  Called everytime that the save button is clicked after editing session text.
  """
  session = Session.objects.get(id=request.session["session"])
  session.content = request.POST["content"]
  print(session.content)
  session.save(update_fields=["content"])
  return render(request, "session_content.html", {
    "session": session,
    "no_cache": random.randint(1, 100000000)
  })
