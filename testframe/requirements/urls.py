from django.urls import path

from . import views

urlpatterns = [
    path('', views.requirements_view, name='requirements_view'),
]
