from django.shortcuts import render,redirect
from . models import Gender
from django.contrib import messages
# from django.http import HttpResponse
# Create your views here.

def index_genders(request):
    genders = Gender.objects.all()
    context = {
        'genders': genders
    }
    return render(request, 'genders/index.html', context)

def create_gender(request):
    return render(request, 'genders/create.html')

def store_gender(request):
    gender = request.POST.get('gender')
    Gender.objects.create(gender=gender)
    messages.success(request,'Gender successfully saved')

    return redirect('/genders')
    # return HttpResponse(gender)

def index_users(request):
    return render(request, 'users/index.html')