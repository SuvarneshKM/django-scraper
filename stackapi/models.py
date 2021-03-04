from django.db import models


class Price(models.Model):
    gram = models.CharField(max_length=50)
    today = models.CharField(max_length=50)
    yesterday = models.CharField(max_length=50)
    change = models.CharField(max_length=50)

    def __str__(self):
        return self.gram


class Pricesilver(models.Model):
    sgram = models.CharField(max_length=50)
    stoday = models.CharField(max_length=50)
    syesterday = models.CharField(max_length=50)
    schange = models.CharField(max_length=50)

    def __str__(self):
        return self.sgram
