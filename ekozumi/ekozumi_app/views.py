from django.shortcuts import render, redirect
from .forms import SignUpForm
 
def registrationPage(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  

            # load the profile instance created by the signal
            user.save()
            #raw_password = form.cleaned_data.get('password1')

            # login user after signing up
            #user = authenticate(username=user.username, password=raw_password)
            #login(request, user)

            # redirect user to home page
            return redirect('zumi_creation')
    else:
        form = SignUpForm()
    return render(request, 'ekozumi_app/register.html', {'form': form})

def homePage(request):
    return render(request, "ekozumi_app/test_home.html")

def zumiCreationPage(request):
    return render(request, "ekozumi_app/zumi_creation.html")
