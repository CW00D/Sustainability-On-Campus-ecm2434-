from django.shortcuts import render, redirect
from .forms import SignUpForm, ZumiCreationForm
from .models import Pet
from django.contrib.auth import authenticate, login
 
def registrationPage(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  

            # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password1')

            # login user after signing up
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)

            # redirect user to zumi creation page
            return redirect('zumi_creation')
    else:
        form = SignUpForm()
    return render(request, 'ekozumi_app/register.html', {'form': form})

def homePage(request):
    return render(request, "ekozumi_app/home.html")

def zumiCreationPage(request):
    if request.method == 'POST':
        form = ZumiCreationForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            pet = Pet(petName = cleaned_data['petName'], petType = cleaned_data['petType'],)
            pet.save()

            current_user = request.user
            print(current_user.pk)
            current_user.profile.petID=pet
            current_user.save()
            return redirect('home_page')
    else:
        form = ZumiCreationForm()
    return render(request, "ekozumi_app/zumi_creation.html", {'form':form})
