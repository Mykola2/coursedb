from django.db import models

class Mymodel(models.Model):
    modname = models.CharField(max_length=30)