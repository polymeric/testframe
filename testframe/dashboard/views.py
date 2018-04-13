from django.shortcuts import render
from projects.models import Projects
from requirements.models import Requirements
from tplans.models import TestPlans

def dashboard_view(request):

  # grab all entries from project table
  projects = Projects.objects.all()
  
  # Trim number of projects passed to client
  # Need server side pagination
  if len(projects) > 50:
      projects = projects[:50]

  # grab all entries from project table
  requirements = Requirements.objects.all()
  # Trim number of projects passed to client
  # Need server side pagination
  if len(requirements) > 50:
    requirements = requirements[:50]

  # grab all entries from project table
  tplans = TestPlans.objects.all()

  # Trim number of projects passed to client
  # Need server side pagination
  if len(tplans) > 50:
    tplans = tplans[:50]

  return render(request, 'dashboard.html', {'projects':projects, 'requirements':requirements, 'tplans': tplans})