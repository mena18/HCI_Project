from django.shortcuts import render,HttpResponse

# Create your views here.



def home(request):
    return render(request,'civil_engineer/home.html')

def table_test(request):
    return render(request,'civil_engineer/table.html')


def pdf_view(request):
    return render(request,'civil_engineer/ViewPdf.html')
