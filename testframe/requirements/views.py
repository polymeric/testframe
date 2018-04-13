from django.shortcuts import render
from requirements.models import Requirements

def requirements_view(request):
  # grab all entries from project table
  requirements = Requirements.objects.all()

  # Trim number of projects passed to client
  # Need server side pagination
  if len(requirements) > 50:
    requirements = requirements[:50]
  return render(request, 'requirements.html', {'requirements': requirements})