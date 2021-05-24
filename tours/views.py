from django.shortcuts import render
from tours.parsing_data_for_departure import pars as departure_pars
from tours.parsing_data_for_tour import pars as tour_pars
from tours.parsing_data_for_random_6_hotels import pars as random_pars


def main_view(request):
    return render(request, 'tours/index.html', context=random_pars())


def departure_view(request, departure):
    return render(request, 'tours/departure.html', context=departure_pars(departure))


def tour_view(request, tour_id):
    return render(request, 'tours/tour.html', context=tour_pars(tour_id))
