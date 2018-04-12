from django.shortcuts import render


def tplans_view(request):
    return render(request, 'tplans.html')