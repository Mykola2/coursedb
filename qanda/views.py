from django.shortcuts import render,redirect, render_to_response
from django.template import RequestContext
from qanda.models import *
from datetime import *



def add(request):
    if request.method == 'GET':
        # print(request)
        return render_to_response('add.html',  context_instance=RequestContext(request))
    if request.POST:
        q = Question()
        q.title = request.POST['title']
        q.content = request.POST['content']
        q.postdate = datetime.now()
        # пользователь который задал  вопрос блеать!
        # нужно решить вопрос с регой и аутентификацией
        q.save()
        tags_list = [Tag(name=t.strip()) for t in request.POST['tags'].split(',')]
        for tag in tags_list:
            tag.save()
        # тут будет tрабла - дублирующиеся теги будут повторяться
        # и снова записываться в базу
        # ИСПРАВИТЬ!!11!
            q.tags.add(tag)
        # q.save()
    return redirect(r'/') # нужен редирект на details нового вопроса




def index(request):
    return render_to_response('index.html', {'obj_list': Question.objects.all()})

def details(request):
    # print(request)
    if request.method == 'GET':
        qst = Question.objects.get(id=int(request.GET['id']))
        return render_to_response('details.html', {'obj': qst},  context_instance=RequestContext(request))
    if request.method == 'POST':
        #create answer, add it to qestion
        # return to the same question's page
        pass
