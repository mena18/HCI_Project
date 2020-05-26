from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from accounts.models import User
# Create your views here.



def login_view(request):
    if request.user.is_authenticated:
        return redirect("/")


    if(request.method=='GET'):
        return render(request,"accounts/login.html")

    email = request.POST['email'];
    password = request.POST['password'];

    try:
        user = User.objects.get(email = email)
        if user.check_password(password):
            login(request,user);
            return redirect("/")
        else:
            return HttpResponse("wrong password");
    except :
        return HttpResponse("user dosen't exists ")



def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("/accounts/login")
    
