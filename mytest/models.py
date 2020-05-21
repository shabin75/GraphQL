from django.db import models

class Test(models.Model):
    name = models.TextField(blank=True)
    age= models.TextField(blank=True)