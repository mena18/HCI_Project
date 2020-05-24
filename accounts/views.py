from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
# Create your views here.



def login_view(request):
    if request.user.is_authenticated:
        return redirect("/")


    if(request.method=='GET'):
        return render(request,"accounts/login.html")

    name = request.POST['username'];
    password = request.POST['password'];

    user = authenticate(request,username=name,password=password)

    if user is not None:
        login(request,user);
        return HttpResponse("loged in")
    else:
        return HttpResponse("failed")



def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("/accounts/login")
