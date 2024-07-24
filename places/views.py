from django.shortcuts import render

from places.models import Categories


def categories(request):
    
    categories = Categories.objects.all()

    context = {
        'title': 'RentVlg - Куда сходить',
        'content': categories,
    }
    return render(request, 'places/place.html', context)