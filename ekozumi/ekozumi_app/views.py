from django.shortcuts import render, redirect
from .forms import SignUpForm
 
def registrationPage(request):
    '''
    Contains the logic for when a user registers
    '''
    # True when a user creates an account
    if request.method == 'POST':
        # Applies the post request to our sign up form
        form = SignUpForm(request.POST)
        # Inbuilt validity checking, matching passwords etc.
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  

            # load the profile instance created by the signal
            user.save()

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
