from django.shortcuts import render


def tcases_view(request):
    return render(request, 'tcases.html')