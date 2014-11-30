from django.shortcuts import render,redirect, render_to_response
from qanda.models import *


def add(request):
    if request.GET:
        q = Question()
        q.title = request.GET['title']
        q.content = request.GET['content']
        # пользователь который задал  вопрос блеать!
        # нужно решить вопрос с регой и аутентификацией
        q.save()
        tags_list = [Tag(name=t.strip()) for t in request.GET['tags'].sprit(',')]
        for tag in tags_list:
            tag.save()
        # тут будет tрабла - дублирующиеся теги будут повторяться
        # и снова записываться в базу
        # ИСПРАВИТЬ!!11!
            q.tags.add(tag)
        q.save()
    #return redirect(r'/') # нужен редирект на details нового вопроса





def index(request):
    return render_to_response('index.html', {'obj_list': Question.objects.all()})

def details(request):
    pass