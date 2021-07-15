from django.shortcuts import render, redirect
from .models import Show
from django.contrib import messages

# Create your views here.
def show(request):
    context = {
        'shows': Show.objects.all()
    }
    return render(request, 'index.html', context)

def new(request):
    return render(request, 'new.html')

def create_show(request):

    errors = Show.objects.show_validator(request.POST)

    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect('/show/new')
    else:
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

def update_show(request, id):
    show = Show.objects.get(id=id)
    show.title = request.POST['mTitle']
    show.network = request.POST['mNetwork']
    show.release_date = request.POST['mDate']
    show.description = request.POST['mDescription']

    errors = Show.objects.show_validator(request.POST)

    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect(f"/show/{show.id}/edit")
    else:
        show.save()
        return redirect('/')

def delete_show(request, id):
    show1 = Show.objects.get(id=id)
    show1.delete()
    return redirect('/')
