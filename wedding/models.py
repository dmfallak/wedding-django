from __future__ import unicode_literals

from django.db import models

class Guest(models.Model):
  invitee = models.CharField(max_length=256)
  attending_max = models.IntegerField(default=0)
  attending_num = models.IntegerField(default=0)
  guest_names = models.CharField(max_length=1024)
  entree1 = models.CharField(max_length=128)
  entree2 = models.CharField(max_length=128)
  hotel = models.BooleanField(default=False)
  shuttle_to_time = models.IntegerField(default=0)
  shuttle_from_time = models.IntegerField(default=0)
  attending = models.BooleanField(default=False)
  responded = models.BooleanField(default=False)

  def __str__(self):
    return self.invitee