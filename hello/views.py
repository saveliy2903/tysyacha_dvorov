import datetime

from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *


def index(request):
    return render(request, "hello/main_page.html")


@login_required
def add_application(request):
    if request.method == "POST":
        application = Application()
        points = 0
        application.quantity_MKD = request.POST.get("quantity_MKD")
        quantity_MKD = int(application.quantity_MKD)
        application.number_people = request.POST.get("number_people")
        application.percentage_of_vote = request.POST.get("percentage_of_vote").replace(',', '.')
        percentage_of_vote = float(application.percentage_of_vote)
        application.yard_area = request.POST.get("yard_area").replace(',', '.')
        application.user = request.user

        if request.POST.get("participation_in_municipal") == 'on':
            application.participation_in_municipal = True
            participation_in_municipal = True
        else:
            application.participation_in_municipal = False
            participation_in_municipal = False

        type_id = request.POST.getlist("types")
        addresses = request.POST.get("address")

        if participation_in_municipal:
            points += 10

        if quantity_MKD >= 3:
            points += 15
        elif quantity_MKD == 2:
            points += 10
        else:
            points += 5

        if 66.67 <= percentage_of_vote <= 80:
            points += 5
        elif 81 <= percentage_of_vote <= 90:
            points += 10
        elif 91 <= percentage_of_vote <= 100:
            points += 15

        application.point = points
        application.save()

        types = Type_jobs.objects.filter(id__in=type_id)
        application.types.set(types)

        addresses = addresses.split(",")
        for address in addresses:
            address = address.split()

            street_name = ''
            for x in address[:-1]:
                street_name = street_name + ' ' + x

            adr = Address(street=street_name, number=address[len(address)-1])
            adr.save()
            application.address.add(adr)
        return HttpResponseRedirect("/")

    types = Type_jobs.objects.all()
    return render(request, "hello/add_application.html", {"types": types})


def delete_applic(request, id):
    try:
        application = Application.objects.get(id=id)
        if request.method == "POST":
            application.delete()
            return HttpResponseRedirect("/")
    except Application.DoesNotExist:
        return HttpResponseNotFound("<h2>Не найдена</h>")


def view_applic(request):
    types = Type_jobs.objects.all()
    streets = Address.objects.all()
    applications = Application.objects.all()
    return render(request, "hello/view_application.html", {"types": types, "streets": streets, "applications": applications})


class SignUp(CreateView):
    form_class = SignUpForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")