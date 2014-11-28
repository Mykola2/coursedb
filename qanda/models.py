from django.db import models



class User(models.Model):
    login = models.CharField(145)
    pwd = models.CharField(145)
    class Meta:
        managed = False
        db_table = 'user'

class Answer(models.Model):
    content = models.TextField()
    postdate = models.DateField()
    user_iduser = models.ForeignKey('User',db_column='user_iduser')
    question_idquestion = models.ForeignKey('Question', db_column='question_idquestion')
    likes = models.ManyToManyField(User)
    class Meta:
        managed = False
        db_table = 'answer'

class Tag(models.Model):
    name = models.CharField(65)
    class Meta:
        managed = False
        db_table = 'tag'

class Question(models.Model):
   title = models.TextField()
   content = models.TextField()
   postdate = models.DateField()
   user_iduser = models.ForeignKey('User',db_column='user_iduser')
   likes = models.ManyToManyField(User) #???
   tags = models.ManyToManyField(Tag)
   class Meta:
        managed = False
        db_table = 'question'