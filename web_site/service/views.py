from multiprocessing import context
from tkinter import SE
from django.shortcuts import render
from .models import Haircuts, Facial, Hand_FootCare


def haircuts(request):
    data = Haircuts.objects.all()
    context = {
        'data': data
    }
    return render(request, 'service/haircuts.html', context)

def facial(request):
    data = Facial.objects.all()
    context = {
        'data': data
    }
    return render(request, 'service/facial.html', context)

def handfoot(request):
    data = Hand_FootCare.objects.all()
    context = {
        'data': data
    }
    return render(request, 'service/handfoot.html', context)

