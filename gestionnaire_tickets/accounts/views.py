from django.shortcuts import render,redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .models import *
from .forms import *

# Create your views here.
def inscription(request):
    if request.method == 'POST':
        form = Inscription_Form(request.POST)
        if form.is_valid():

            utilisateur = form.save()

            profil = Profil.objects.create(utilisateur=utilisateur)
            profil.genere_numero_employe()
            profil.save()

            login(request, utilisateur)
            return redirect('liste_tickets')

    else:
        form = Inscription_Form()

    return render(request, 'inscription.html', {'form':form})


def connexion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            utilisateur = authenticate(request, username=username, password=password)
            if utilisateur is not None:
                login(request, utilisateur)
                return redirect('inscription')
    else:
        form = AuthenticationForm()
    
    return render(request, 'connexion.html', {'form':form})


def deconnexion(request):
    logout(request)
    return redirect('inscription')