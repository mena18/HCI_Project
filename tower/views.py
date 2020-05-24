from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required
from accounts.models import User
from .models import *
from .service import seperate_users,levels_data
import random
from  datetime import datetime,timedelta
import time

# Create your views here.


# must be changed to 3 seperate functions  #
@login_required
def home(request):
    if(request.user.is_engineer):
        return engineer_home(request)
    elif(request.user.is_foreman):
        return foreman_home(request)
    elif(request.user.is_worker):
        return worker_home(request)





# Engineering
def engineer_home(request):
    users = User.objects.all()
    context = seperate_users(users)

    return render(request,'engineer/home.html',context)

def engineer_levels(request):
    levels = levels_data();
    return render(request,'engineer/levels.html',levels)

def engineer_level(request,num):
    return render(request,'engineer/level.html')


def engineer_workers(request):
    workers = User.objects.filter(is_worker = True);
    return render(request,'engineer/workers.html',{'workers':workers})

def engineer_foremen(request):
    foremen = User.objects.filter(is_foreman = True);
    print("*"*100,len(foremen))
    return render(request,'engineer/foremen.html',{'foremen':foremen})





# Foreman

def foreman_home(request):
    return render(request,"forman/home.html");

def foreman_levels(request,num=None):
    return render(request,"forman/level.html");




# workers
def worker_home(request):
    return render(request,"worker/home.html");






# testing

def add_workers(request):
    for i in range(30):
        user = User()
        user.username = f'worker_{i+1}'
        user.set_password('123')
        user.is_worker=True
        if(i%3==0):
            user.type = 'painter'
        elif(i%3==1):
            user.type = 'cleaner'
        else:
            user.type = 'plumber'
        user.save()
    return HttpResponse("done");



def add_operations(request):
    operations_types = Operation_type.objects.all()
    for i in range(100):
        operation = Operation()
        operation.type = operations_types[random.randint(0,len(operations_types)-1)]
        operation.level_id = random.randint(1,10)
        operation.must_finish = random.randint(1,60)
        operation.deadline = datetime.now() + timedelta(days = random.randint(5,30))
        operation.save()
        if(i%10==0):
            print(f"Patch {i*10}")


    return HttpResponse("done");
