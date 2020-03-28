from django.db import models

class University(models.Model):
    name = models.CharField(max_length=128)
    abbreviation = models.CharField(max_length=10)
    ownership = models.CharField(max_length=10)
    n_students = models.IntegerField()
    n_staff = models.IntegerField()
    n_profs = models.IntegerField()
    state = models.ForeignKey('State', on_delete=models.CASCADE,)
    city = models.CharField(max_length=64)
    budget = models.IntegerField()
    corona_page = models.CharField(max_length=600)
    main_page = models.CharField(max_length=12)

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=128)
    abbreviation = models.CharField(max_length=5)
    country = models.ForeignKey('Country', on_delete=models.CASCADE,)
    bip = models.IntegerField()

    def __str__(self):
        return self.abbreviation

class Country(models.Model):
    name = models.CharField(max_length=128)
    abbreviation = models.CharField(max_length=3)
    bip = models.IntegerField()

    def __str__(self):
        return self.abbreviation

