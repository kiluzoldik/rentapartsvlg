from django.shortcuts import render

from places.models import Places


def categories(request, category_slug):
    
    if category_slug == 'all':
        places = Places.objects.all()
    else:
        places = Places.objects.filter(category__slug=category_slug)

    context = {
        'title': 'RentVlg - Куда сходить',
        'places': places,
    }
    return render(request, 'places/place.html', context)