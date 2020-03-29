from django.db import models

class University(models.Model):
    name = models.CharField(max_length=128)
    abbreviation = models.CharField(max_length=10)
    kind = models.CharField(max_length=32)
    ownership = models.CharField(max_length=10)
    n_students = models.IntegerField()
    n_staff = models.IntegerField()
    n_profs = models.IntegerField()
    state = models.ForeignKey('State', on_delete=models.CASCADE,)
    city = models.CharField(max_length=64)
    budget = models.IntegerField()
    corona_page = models.CharField(max_length=600)
    main_page = models.CharField(max_length=128)
    page_quality = models.CharField(max_length=12)

    def __str__(self):
        return self.name

class Corporation(models.Model):
    name = models.CharField(max_length=128)
    kind = models.CharField(max_length=32)
    n_employees = models.IntegerField()
    state = models.ForeignKey('State', on_delete=models.CASCADE,)
    city = models.CharField(max_length=64)
    stock_price = models.FloatField()
    corona_page = models.CharField(max_length=600)
    main_page = models.CharField(max_length=128)
    page_quality = models.CharField(max_length=12)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=128)
    abbreviation = models.CharField(max_length=3)
    bip = models.IntegerField()
    people = models.IntegerField()

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=128)
    abbreviation = models.CharField(max_length=8)
    country = models.ForeignKey('Country', on_delete=models.CASCADE,)
    people = models.IntegerField()

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=128)
    state = models.ForeignKey('State', on_delete=models.CASCADE,)
    people = models.IntegerField()

    def __str__(self):
        return self.name

class Measure(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Implemented(models.Model):
    entity_type = models.IntegerField() # Should be 0 for unis, 1 for corps
    entity_id = models.ForeignKey("University", on_delete=models.CASCADE)
    measure = models.ForeignKey("Measure", on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return self.name
