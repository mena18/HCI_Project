from django.shortcuts import render,HttpResponse,redirect,reverse
from django.contrib.auth.decorators import login_required
from accounts.models import User
from .models import *
from .service import seperate_users,levels_data
from django.core import serializers
import random
from  datetime import datetime,timedelta
import time

# Create your views here.


@login_required
def home(request):
    if(request.user.is_engineer):
        return engineer_home(request)
    elif(request.user.is_foreman):
        return foreman_home(request)
    elif(request.user.is_worker):
        return worker_home(request)


# some api calls
def get_operations(request,level=None):
    pass

def get_progress(request,level=None):
    pass

def get_workers_progress(request,level=None):
    pass



# -------------------------   Engineer Actions  -------------------------
def engineer_home(request):
    users = User.objects.all()
    context = seperate_users(users)

    return render(request,'engineer/home.html',context)

def engineer_levels(request):
    context={}
    context['levels'] = levels_data();
    context['foremen'] = User.objects.filter(is_foreman=True);
    return render(request,'engineer/levels.html',context)

def engineer_level(request,num):
    level = Level.objects.get(name=num)
    operation_types = Operation_type.objects.filter(level=level)
    return render(request,'engineer/level.html',{'operation_types':operation_types,'level':level})


def engineer_workers(request):
    workers = User.objects.filter(is_worker = True);
    for i in workers:
        print(i.__dict__)
    return render(request,'engineer/workers.html',{'workers':workers})

def engineer_foremen(request):
    foremen = User.objects.filter(is_foreman = True);
    print("*"*100,len(foremen))
    return render(request,'engineer/foremen.html',{'foremen':foremen})



def remove_foreman(request,level_num):
    level = Level.objects.get(name = level_num)
    level.foreman = None
    level.save()
    return redirect(reverse('tower:engineer_levels'))


def assign_foreman(request):
    if(request.method!='POST'):
        return HttpResponse("forbidden")

    level_num = request.POST['level_num']
    level = Level.objects.get(name=level_num)
    level.foreman_id = request.POST['foreman']
    level.save()


    return redirect(reverse('tower:engineer_levels'))


def add_worker(request):
    if(request.method=='POST'):
        worker = User()
        worker.email = request.POST['email'];
        worker.is_worker = True
        worker.set_password(request.POST['password'])
        worker.first_name = request.POST['first_name'];
        worker.last_name = request.POST['last_name'];
        worker.type = request.POST['type'];
        worker.save()
        return redirect(reverse("tower:engineer_workers"))

    return HttpResponse('forbidden')

def edit_worker(request):
    if(request.method=='POST'):
        worker = User.objects.get(id=request.POST['id'])
        worker.email = request.POST['email'];
        if request.POST['password']:
            worker.set_password(request.POST['password'])
        worker.first_name = request.POST['first_name'];
        worker.last_name = request.POST['last_name'];
        worker.type = request.POST['type'];
        worker.save()
        return redirect(reverse("tower:engineer_workers"))

    return HttpResponse('forbidden')

def delete_worker(request):
    if request.method == "POST":
        lis = request.POST.getlist('id[]')
        User.objects.filter(id__in=lis).delete()
        return redirect(reverse("tower:engineer_workers"))

    return HttpResponse('forbidden')


def add_foreman(request):
    if(request.method=='POST'):
        worker = User()
        worker.email = request.POST['email'];
        worker.username = request.POST['email'];
        worker.is_foreman = True
        worker.set_password(request.POST['password'])
        worker.first_name = request.POST['first_name'];
        worker.last_name = request.POST['last_name'];
        worker.save()
        return redirect(reverse("tower:engineer_foremen"))

    return HttpResponse('forbidden')

def edit_foreman(request):
    if(request.method=='POST'):
        worker = User.objects.get(id=request.POST['id'])
        worker.email = request.POST['email'];
        if request.POST['password']:
            worker.set_password(password)
        worker.first_name = request.POST['first_name'];
        worker.last_name = request.POST['last_name'];
        worker.save()
        return redirect(reverse("tower:engineer_workers"))

    return HttpResponse('forbidden')

def delete_foreman(request):
    if request.method == "POST":
        lis = request.POST.getlist('id[]')
        User.objects.filter(id__in=lis).delete()
        return redirect(reverse("tower:engineer_foremen"))

    return HttpResponse('forbidden')


# -------------------------   End Engineer Actions  -------------------------






# -------------------------   Foreman Actions  -------------------------

def foreman_home(request):
    levels = Level.objects.filter(foreman = request.user);
    context = {"levels":levels}
    return render(request,"foreman/home.html",context);

def foreman_levels(request,num):
    levels = Level.objects.filter(foreman = request.user);
    level_num = Level.objects.get(name=num)
    operation_types = Operation_type.objects.filter(level=level_num)
    context = {"level_num":level_num,'levels':levels,"operation_types":operation_types}
    return render(request,"foreman/level.html",context);

# -------------------------   End Foreman Actions  -------------------------







# -------------------------   Workers Actions  -------------------------
def worker_home(request):
    return render(request,"worker/home.html");


# -------------------------   End Workers Actions  -------------------------





# testing

def download_operations(request):
    operations = Operation.objects.all();
    operations = serializers.serialize('json', operations)
    return HttpResponse(operations, content_type="text/json-comment-filtered")


def add_workers(request):
    for i in range(8):
        user = User()
        user.username = f'new_foreman{i+1}'
        user.email = f'new_foreman@new_foreman.com{i+1}'
        user.first_name = "Foreman"
        user.last_name = str(i+1)
        user.is_foreman = True
        user.set_password('123')
        user.save()
    return HttpResponse("done");
    # for i in range(30):
    #     user = User()
    #     user.username = f'worker_{i+1}'
    #     user.set_password('123')
    #     user.is_worker=True
    #     if(i%3==0):
    #         user.type = 'painter'
    #     elif(i%3==1):
    #         user.type = 'cleaner'
    #     else:
    #         user.type = 'plumber'
    #     user.save()
    # return HttpResponse("done");



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
