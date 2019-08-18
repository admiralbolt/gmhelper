from django.db import models

class Tag(models.Model):
  """An abstract class for classifying data items."""
  name = models.CharField(max_length=64)
  flavor = models.TextField(default=None, blank=True)

  def __str__(self):
    return self.name

class Letter(models.Model):
  """Represents a letter the players receive.

  The name flavor and author of the letter will be private information, only the
  text of the letter will be displayed to the client.
  """
  name = models.CharField(max_length=255)
  flavor = models.TextField(default=None, blank=True)
  author = models.CharField(max_length=255)
  text = models.TextField()

  def __str__(self):
    return self.name

class Lore(models.Model):
  """A piece of lore. Similar to a letter, but not used for displaying."""
  name = models.CharField(max_length=255)
  flavor = models.TextField(default=None, blank=True)
  text = models.TextField()

  def __str__(self):
    return self.name

class Image(models.Model):
  """It's an image. Literally read the name you fucking ape."""
  name = models.CharField(max_length=255)
  flavor = models.TextField(default=None, blank=True)
  image_file = models.FileField(upload_to="images/")

  def __str__(self):
    return self.name

class Song(models.Model):
  """Music makes the world go round."""
  name = models.CharField(max_length=255)
  flavor = models.TextField(default=None, blank=True)
  tags = models.ManyToManyField(Tag, blank=True)
  # Whether or not to loop the song continuously. This is generally true for
  # things like battle & ambient music.
  loop = models.BooleanField(default=False)
  sound_file = models.FileField(upload_to="music/")

  def __str__(self):
    return self.name

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

  # Each of the data item models is accounted for here. Sessions may share data
  # items across them, hence the ManyToMany.
  letters = models.ManyToManyField(Letter, blank=True)
  lores = models.ManyToManyField(Lore, blank=True)
  images = models.ManyToManyField(Image, blank=True)
  songs = models.ManyToManyField(Song, blank=True)

  def __str__(self):
    return self.name
