from django.shortcuts import render


def index(request):
    context = {
        'title': 'RentVlg - Главная'
    }
    return render(request, 'main/index.html', context)
