from django.db import models

# Create your models here.


class Photofon(models.Model):
    size = models.CharField(max_length=100, blank=False)
    color = models.CharField(max_length=50, blank=False)
    image = models.ImageField(upload_to='fotofon/', blank=False)
    price = models.IntegerField(default=0)
    short_description = models.CharField(max_length=300, blank=False, default=0)

    def __str__(self):
        self.name = self.color + ',' + self.size
        return self.name


class Mirror(models.Model):
    size = models.CharField(max_length=100, blank=True)
    color = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='mirror/', blank=False)
    price = models.IntegerField(default=0)
    short_description = models.CharField(max_length=300, blank=False, default=0)

    def __str__(self):
        self.name = self.color + ',' + self.size
        return self.name
