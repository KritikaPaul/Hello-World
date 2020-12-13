from django.shortcuts import render,redirect
from django.http import HttpResponse
from country.models import country
from .forms import countryForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    country_list = country.objects.all()
    context ={
        'country_list':country_list
    }
    return render(request,'country/index.html',context)

def details(request,country_id):
    countrys = country.objects.get(id=country_id)
    return render(request,'country/details.html',{'country':countrys})

@login_required(login_url="/account/login/")
def add_country(request):
    if request.method == "POST":
        country_name=request.POST.get('country_name',)
        currency=request.POST.get('currency',)
        country_image=request.FILES['country_image']

        countrys = country(country_name=country_name,currency=currency,country_image=country_image)
        countrys.save()

    return render(request,'country/add_country.html')

def update(request,id):
    countrys = country.objects.get(id=id)
    form = countryForm(request.POST or None, request.FILES, instance=country)
    if form.is_valid():
        form.save()
        return redirect('/country')
    return render(request,'country/edit.html',{'form':form,'country':countrys})

def delete(request,id):
    if request.method == "POST":
        countrys=country.objects.get(id=id)
        countrys.delete()
        return redirect('/country')
    return render(request,'country/delete.html')
