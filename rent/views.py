from django.shortcuts import render


def rent(request):
    context = {
        'title': 'RentVlg - Заселение'
    }
    return render(request, 'rent/rent.html', context)