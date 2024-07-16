from django.shortcuts import render


def index(request):
    context = {
        'title': 'RentVlg'
    }
    return render(request, 'main/index.html', context)
