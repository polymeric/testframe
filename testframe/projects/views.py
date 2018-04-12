from django.shortcuts import render
from projects.models import Projects


def projects_view(request):
    projects = Projects.objects.all()
    # Trim number of projects passed to client
    # Need server side pagination
    if len(projects) > 50:
        projects = projects[:50]
    return render(request, 'projects.html', {'projects':projects})

