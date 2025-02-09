from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from K_Competition_Mng.models import competition, register
# Create your views here.

def home (request):
    return render(request, 'home/index.html')

def competitions(request):
    competitions = competition.objects.all()
    template = loader.get_template('home/competition/competitions.html')
    context = {
        'competition': competitions,
    }
    return HttpResponse(template.render(context, request))

def competition_edit(request):
    competition_edit = competition.objects.get(id = 1)
    template = loader.get_template('home/competition/competition-edit.html')
    context = {
        'competition': competition,
    }
    return HttpResponse(template.render(context, request))

def account(request):
    account = register.objects.all()
    template = loader.get_template('home/register/account.html')
    context = {
        'register': account,
    }
    return HttpResponse(template.render(context, request))

def account_edit(request):
    account_edit = register.objects.get(id = 1)
    template = loader.get_template('home/register/account-edit.html')
    context = {
        'register': register,
    }
    return HttpResponse(template.render(context, request))

def koi(request):
    koi = register.objects.all()
    template = loader.get_template('home/register/koi.html')
    context = {
        'register': account,
    }
    return HttpResponse(template.render(context, request))

def koi_edit(request):
    koi_edit = register.objects.get(id = 1)
    template = loader.get_template('home/register/koi-edit.html')
    context = {
        'register': register,
    }
    return HttpResponse(template.render(context, request))