from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('^power/',views.index, name='power'),
]
