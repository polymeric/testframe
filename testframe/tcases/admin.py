from django.contrib import admin
from tcases.models import TestCases
from tcases.models import TestCaseCategories

admin.site.register(TestCaseCategories)
admin.site.register(TestCases)