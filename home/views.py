from django.shortcuts import render
from . models import Usermodel
import re
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'auth/index.html')

def home(request):
    return render(request, 'informations/home.html')

def about(request):
    return render(request, 'informations/about.html')

def service(request):
    return render(request, 'informations/service.html')

def contact(request):
    if request.method == 'GET':
        return render(request, 'informations/contact.html')
    if request.method == 'POST':
        Name = request.POST.get('Name')
        Email = request.POST.get('Email')
        Message = request.POST.get('Message')
        Phone = request.POST.get('Phone')
        Birthday = request.POST.get('Birthday')
        Address = request.POST.get('Address')
        Usermodel.objects.all().values()
        user = Usermodel(name=Name, email=Email, message=Message, phone=Phone, birthday=Birthday, address=Address)
        if not re.search(r'^\w+$', Name) or not re.search(r'^\w+$', Message) or not re.search(r'^\w+$',Address):
            context = {
                'demo' : 1,
            }
            # return HttpResponse
            return render(request, 'informations/contact.html', context)

        else:
            # context = {
            #     'demo' : 2,
            # }
            user.save()
            return render(request, 'informations/contact.html')

def experience(request):
    context = {
        'greet' : 1,
    }
    return render(request, 'informations/experience.html', context)