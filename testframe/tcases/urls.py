from django.urls import path

from . import views

urlpatterns = [
    path('', views.tcases_view, name='tcases_view'),
]
