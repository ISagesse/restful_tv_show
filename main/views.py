from django.shortcuts import render, redirect
from .models import Show
from datetime import datetime

# Create your views here.
def show(request):
    context = {
        'shows': Show.objects.all()
    }
    return render(request, 'index.html', context)

def new(request):
    return render(request, 'new.html')

def create_show(request):
    Show.objects.create(
        title = request.POST['mTitle'],
        network = request.POST['mNetwork'],
        release_date = request.POST['mDate'],
        description = request.POST['mDescription']
    )

    return redirect('/')


def one_show(request, id):
    show = Show.objects.get(id=id)
    context = {
        'show': show
    }
    return render(request, 'show.html', context)

def edit_show(request, id):
    show = Show.objects.get(id=id)
    context = {
        'show': show
    }
    return render(request, 'update.html', context)

def update_show(request):
    title = request.POST['title']
    network = request.POST['network']
    date = request.POST['date']
    description = request.POST['description']

    Show.objects.update(title=f"{title}", network=f"{network}", release_date=f"{date}", description=f"{description}")
    return redirect('/')

def delete_show(request, id):
    show1 = Show.objects.get(id=id)
    show1.delete()
    return redirect('/')
