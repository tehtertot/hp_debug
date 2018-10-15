from django.shortcuts import render, redirect
from .models import Wand

def index(request):
    """show a page with all the wands"""
    context = {
        "all_wands": Wand.objects.all()
    }
    return render(request, "ollivanders/index.html")

def show_add(request):
    """ show a page with the form to add a wand"""
    return render(request, "ollivanders/show.html")

def add_to_db(request):
    """ process the submission of a new wand"""
    if request.method == "POST":
        Wand.objects.create(core=request.POST["core"], length=request.POST["length"])
    return redirect("/")