from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from gm2m import GM2MField

class Tag(models.Model):
  """An abstract class for classifying data items."""
  name = models.CharField(max_length=64)
  flavor = models.TextField(default=None, blank=True)

  def __str__(self):
    return self.name

class DataItem(models.Model):
  """Abstract super class for all data items. Contains name & flavor only."""
  name = models.CharField(max_length=255)
  flavor = models.TextField(default=None, blank=True)

  def __str__(self):
    return self.name

  class Meta:
    abstract = True

class Letter(DataItem):
  """Represents a letter the players receive.

  The name flavor and author of the letter will be private information, only the
  text of the letter will be displayed to the client.
  """
  author = models.CharField(max_length=255)
  text = models.TextField()
  items = GenericRelation("SessionItem", related_query_name="letter")

class Lore(DataItem):
  """A piece of lore. Similar to a letter, but not used for displaying."""
  text = models.TextField()
  items = GenericRelation("SessionItem", related_query_name="lore")

class Image(DataItem):
  """It's an image. Literally read the name you fucking ape."""
  image_file = models.FileField(upload_to="images/")
  items = GenericRelation("SessionItem", related_query_name="image")

class Song(DataItem):
  """Music makes the world go round."""
  tags = models.ManyToManyField(Tag, blank=True)
  # Whether or not to loop the song continuously. This is generally true for
  # things like battle & ambient music.
  loop = models.BooleanField(default=False)
  sound_file = models.FileField(upload_to="music/")
  items = GenericRelation("SessionItem", related_query_name="song")

class Campaign(models.Model):
  """A Campaign!

  A campaign won't have much data itself, but it will be comprised of multiple
  sessions. The actual session objects themselves will hold the necessary data.
  """
  name = models.CharField(max_length=255)
  flavor = models.TextField(default=None, blank=True)

  def __str__(self):
    return self.name

class Session(models.Model):
  """A Session!

  This is the real meat of the app. Sessions will contain two primary things:
  1. A whole bunch of data items: images to show to players, songs to play...
  2. A content field for planning out the session.
  """
  name = models.CharField(max_length=255)
  campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
  flavor = models.TextField(default=None, blank=True)
  content = models.TextField(default=None, blank=True)
  # Used for a post-session reflection.
  reflection = models.TextField(default=None, blank=True)

  def __str__(self):
    return self.name

class SessionItem(models.Model):
  session = models.ForeignKey(Session, on_delete=models.CASCADE)
  # By default generic relations look for a field named 'content_type' and
  # 'object_id'.
  content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
  object_id = models.PositiveIntegerField()
  item = GenericForeignKey()
  order = models.PositiveIntegerField()
