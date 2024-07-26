from django.shortcuts import render

from places.models import Places


def categories(request):
    
    places = Places.objects.all()

    context = {
        'title': 'RentVlg - Куда сходить',
        'places': places,
    }
    return render(request, 'places/place.html', context)