from django.urls import path
from . import views

urlpatterns = [
    path('haircuts', views.haircuts, name='haircut'),
    path('facial', views.facial, name='facial'),
    path('manikyur-pedikyur', views.handfoot, name='handfoot')
]