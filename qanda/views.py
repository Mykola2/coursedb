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
        # add reference to user who's asked the qestion
        # make normal rega and login bldjad
        q.save()
        tags_list = [Tag.objects.get_or_create(name=t.strip())[0] for t in request.POST['tags'].split(',')]
        for tag in tags_list:
            tag.save()
        # VANGA : repeated tags go to the db anyway
        # FIX DIS SHIT!!!111
            q.tags.add(tag)
        # q.save()
    return render_to_response('details.html', {'obj': q})




def index(request):
    try:
        st = request.GET['search_tag']
        olist = Question.objects.filter(tags__id__contains=st)
    except:
        olist = Question.objects.all()
    return render_to_response('index.html', {'obj_list': olist})




def details(request):
    # print(request)
    if request.method == 'GET':
        qst = Question.objects.get(id=int(request.GET['id']))
        return render_to_response('details.html', {'obj': qst},  context_instance=RequestContext(request))
    if request.method == 'POST':
        #create answer, add it to qestion
        # return to the same question's page
        pass
