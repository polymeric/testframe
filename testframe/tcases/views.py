from django.shortcuts import render
from tcases.models import TestCases, TestCaseCategories

def tcases_view(request):
  # grab all entries from project table
  tcases = TestCases.objects.all()

  # Trim number of projects passed to client
  # Need server side pagination
  if len(tcases) > 50:
    tplans = tcases[:50]
  return render(request, 'tcases.html', {'tcases':tcases})