from django.db import models

class SongTag(models.Model):
  name = models.CharField(max_length=64)
  flavor = models.TextField(default=None, blank=True)

  def __str__(self):
    return self.name


class Song(models.Model):
  name = models.CharField(max_length=255)
  flavor = models.TextField(default=None, blank=True)
  tags = models.ManyToManyField(SongTag, blank=True)
  loop = models.BooleanField(default=False)
  sound_file = models.FileField(upload_to="music/")

  def __str__(self):
    return self.name
