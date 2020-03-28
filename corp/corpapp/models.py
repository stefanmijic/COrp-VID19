from django.db import models

class University(models.Model):
    name = models.CharField(max_length=128)
    nstudents = models.IntegerField()
    nstaff = models.IntegerField()
