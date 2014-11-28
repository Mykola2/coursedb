from django.db import models

class Mymodel(models.Model):
    modname = models.CharField(max_length=30)
    asd = models.CharField(max_length=666)
    asd1 = models.CharField(max_length=666)


class  tts(Mymodel, list):
    #just another test model
    pass