from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import Packageform, trackerform, CustomerRegisterform
from .models import Package


import random 

# Create your views here.


def home(request):
    
        
    return render(request, 'service/home.html')



def Register(request):

    form = Packageform()

    if request.method == 'POST':
        form = Packageform(request.POST or None)
        if form.is_valid():
            form.save()                   
            
            return redirect('home')    
        else:
            return redirect('register')
    else:
        return render(request, 'service/register.html', {'form': form})


 

def trackitem(request):
    
    if request.method == 'POST':
        form = trackerform(request.POST)

        if form.is_valid():
            trackid    = form.cleaned_data['id']
            details    = Package.objects.filter(trackingId=trackid)
            context    = {"details":details}
            return render(request, 'service/trackpage.html', context)
        else:
            form = trackerform()
    
    else:
        form = trackerform()
   
    return render(request, 'service/trackpage.html', {'form':form})




def customer(request):

    form = CustomerRegisterform()

    if request.method == 'POST':
        form = CustomerRegisterform(request.POST)

        if form.is_valid():
            form.save()

            return messages.info(request, 'Registrations Successful')
    else:
        form = CustomerRegisterform()
    context  = {'form':form}

    return render(request, 'service/customer.html', context)


def trackgenerator():
    num     = random.randint(00000, 99999)
    comname = 'LR'
    id      = str(num) + comname

    trackid = Package.objects.create(trackingId=id)
    trackid.save()
    

def navbar(request):


    return render(request, 'service/navbar.html')
    
def main(request):
    
    return render(request, 'service/main.html')
