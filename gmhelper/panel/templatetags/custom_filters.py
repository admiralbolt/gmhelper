import re

from bs4 import BeautifulSoup
from django import template
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from panel.models import City

register = template.Library()

@register.filter(name="class_name")
def class_name(value):
  return value.__class__.__name__

@register.filter(name="custom_views")
def custom_views(html_text):
  soup = BeautifulSoup(html_text, "html.parser")
  for city_tag in soup.find_all("city"):
    city = City.objects.get(id=city_tag["id"])
    new_city_tag = BeautifulSoup(render_to_string("city.html", {"city": city}))
    city_tag.replace_with(BeautifulSoup(render_to_string("city.html", {"city": city})))
  regex = re.compile(r"\n+", re.IGNORECASE)
  for item in soup:
    item_text = str(item).strip()
    if not item_text.startswith("<"):
      item.replace_with(BeautifulSoup(item_text.replace("\n", "<br />")))
  return soup
