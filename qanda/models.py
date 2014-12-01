from django.db import models



class User(models.Model):
    login = models.CharField(max_length=145)
    pwd = models.CharField(max_length=145)




class Tag(models.Model):
    name = models.CharField(max_length=65, unique=True)


class Question(models.Model):
   title = models.TextField()
   content = models.TextField()
   postdate = models.DateField()
   user_iduser = models.ForeignKey('User', db_column='user_iduser', default=0)
   likes = models.ManyToManyField(User,related_name="question_likes", default=0) #???
   tags = models.ManyToManyField(Tag,related_name="question_tags")

class Answer(models.Model):
    content = models.TextField()
    postdate = models.DateField()
    user_iduser = models.ForeignKey('User',db_column='user_iduser')
    question_idquestion = models.ForeignKey('Question', db_column='question_idquestion')
    likes = models.ManyToManyField(User, related_name="answer_likes")
