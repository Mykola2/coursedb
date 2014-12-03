from django.shortcuts import render,redirect, render_to_response
from django.template import RequestContext
from qanda.models import *
from datetime import *
from forms import UserForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

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


def register(request):
    context = RequestContext(request)
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print user_form.errors,
    else:
        user_form = UserForm()

    return render_to_response(
            'register.html',
            {'user_form': user_form, 'registered': registered},
            context)

def login(request):
    context = RequestContext(request)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                auth_login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    else:
        return render_to_response('login.html', {}, context)

@login_required
def user_logout(request):
    logout(request)
    return render_to_response('add.html')

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
