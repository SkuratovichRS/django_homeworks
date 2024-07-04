import csv

from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from pagination.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    data = []
    with open(BUS_STATION_CSV, encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            data.append(row)
    paginator = Paginator(data, 5)
    page_number = int(request.GET.get("page", 1))
    page = paginator.get_page(page_number)
    stations = [{"Name": station.get("Name"),
                 "Street": station.get("Street"),
                 "District": station.get("District")} for station in page]
    context = {
        'bus_stations': stations,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
