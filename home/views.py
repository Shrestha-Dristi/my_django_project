from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from home.models import Student

# Create your views here.
def home(request):
    # print("Hello, Everybody")
    return HttpResponse("Hello Everyone")

def aboutus(request,data):
    return HttpResponse(f'{datetime.now()} <b>Hello {data}</b>')

def parms(request):
    data = request.GET.get('data', 'Broadway')
    return HttpResponse(f'{datetime.now()} <b>Hello {data} </b>')

def home_template(request):
    # company = "Cedar Gate"
    # contact = 9820114363
    # country = "Nepal"
    # data = {}
    # data['company'] = company
    # data['contact'] = contact
    # data['country'] = country

    student = Student.objects.all()
    context = {
        "student":student
    }

    # return HttpResponse(name, data)
    return render(request, 'student/index.html', context)

def home_redirect(request):
    return redirect('/admin')