from django.db import models

class University(models.Model):
    name = models.CharField(max_length=128)
    nstudents = models.IntegerField()
    nstaff = models.IntegerField()

    def __str__(self):
        return self.name
