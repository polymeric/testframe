from django.shortcuts import render


def requirements_view(request):
    return render(request, 'requirements.html')