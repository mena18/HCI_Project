from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.


# must be changed to 3 seperate functions  #
@login_required
def home(request):
    if(request.user.is_engineer):
        return render(request,'engineer/home.html')
    elif(request.user.is_foreman):
        return render(request,'foreman/home.html')
    elif(request.user.is_worker):
        return render(request,'worker/home.html')


def engineer_workers(request):
    return render(request,'engineer/workers.html')


def table_test(request):
    return render(request,'components/table.html')


def pdf_view(request):
    return render(request,'components/ViewPdf.html')
