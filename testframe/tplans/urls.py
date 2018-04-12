from django.urls import path

from . import views

urlpatterns = [
    path('', views.tplans_view, name='tplans_view'),
]
