from django.shortcuts import render, redirect
from .models import Visitor
from .forms import VisitorForm

# Creating views.
def welcome(request):
    return render(request, "welcome.html")


def load_form(request):
    form = VisitorForm
    return render(request, "index.html", {'form':form})


def add(request):
    form = VisitorForm(request.POST)
    form.save()
    return redirect('/show')


def show(request):
    visitor = Visitor.objects.all
    return render(request, 'show.html', {'visitor':visitor})


def edit(request, id):
    visitor = Visitor.objects.get(id=id)
    return render(request, 'edit.html', {'visitor': visitor})


def update(request, id):
    visitor = Visitor.objects.get(id=id)
    form = VisitorForm(request.POST, instance=visitor)
    form.save()
    return redirect('/show')


def delete(request, id):
    visitor = Visitor.objects.get(id=id)
    visitor.delete()
    return redirect('/show')

