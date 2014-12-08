from django.db import models
from django.contrib.auth.models import User


class User1(User):
    username1= models.CharField(max_length=145)
    password1 = models.CharField(max_length=145)




class Tag(models.Model):
    name = models.CharField(max_length=65, unique=True)


class Question(models.Model):
   title = models.TextField()
   content = models.TextField()
   postdate = models.DateField()
   user_iduser = models.ForeignKey(User)
   likes = models.ManyToManyField(User,related_name="question_likes") #???
   tags = models.ManyToManyField(Tag,related_name="question_tags")

class Answer(models.Model):
    content = models.TextField()
    postdate = models.DateField()
    user_iduser = models.ForeignKey(User)
    question_idquestion = models.ForeignKey('Question', db_column='question_idquestion', related_name='answers')
    likes = models.ManyToManyField(User, related_name="answer_likes")
