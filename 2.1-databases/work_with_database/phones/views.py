from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones_objects = Phone.objects.all()
    if request.GET.get("sort") == "name":
        phones_objects = list(phones_objects)
        phones_objects.sort(key=lambda x: x.name)
    elif request.GET.get("sort") == "min_price":
        phones_objects = list(phones_objects)
        phones_objects.sort(key=lambda x: x.price)
    elif request.GET.get("sort") == "max_price":
        phones_objects = list(phones_objects)
        phones_objects.sort(key=lambda x: x.price, reverse=True)
    context = {"phones": phones_objects}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {"phone": phone}
    return render(request, template, context)
