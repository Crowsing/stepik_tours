from django.shortcuts import render


def main_view(request):
    return render(request, 'tours/index.html')


def departure_view(request):
    return render(request, 'tours/departure.html')


def tour_view(request):
    return render(request, 'tours/tour.html')