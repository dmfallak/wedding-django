from __future__ import unicode_literals

from django.db import models

class Guest(models.Model):
  invitee = models.CharField(max_length=256)
  attending_max = models.IntegerField()
  attending_num = models.IntegerField(default=0, blank=True)
  guest_names = models.CharField(max_length=1024,default="", blank=True)
  entree1 = models.CharField(max_length=1024,default="", blank=True)
  entree2 = models.CharField(max_length=1024,default="", blank=True)
  side = models.CharField(max_length=1024,default="", blank=True)
  hotel = models.BooleanField(default=False, blank=True)
  shuttle_to_time = models.IntegerField(default=0, blank=True)
  shuttle_from_time = models.IntegerField(default=0, blank=True)
  attending = models.BooleanField(default=False, blank=True)
  responded = models.BooleanField(default=False, blank=True)

  def __str__(self):
    return self.invitee

class ShuttleFrom(models.Model):
  time = models.CharField(max_length=32)
  seats_max = models.IntegerField(default=0)
  seats_free = models.IntegerField(default=0)

  def __str__(self):
    return self.time

class ShuttleTo(models.Model):
  time = models.CharField(max_length=32)
  seats_max = models.IntegerField(default=0)
  seats_free = models.IntegerField(default=0)

  def __str__(self):
    return self.time