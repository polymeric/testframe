from django.shortcuts import render
from tplans.models import TestPlans

def tplans_view(request):
  # grab all entries from project table
  tplans = TestPlans.objects.all()

  # Trim number of projects passed to client
  # Need server side pagination
  if len(tplans) > 50:
    tplans = tplans[:50]
  return render(request, 'tplans.html', {'tplans': tplans})