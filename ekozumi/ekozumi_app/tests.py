from django.test import TestCase
from .forms import SignUpForm, ZumiCreationForm
from django.contrib.auth import authenticate, login
from .models import Pet
from django.urls import reverse

"""
Tests for ekozumi_app
Author: Oscar Klemenz
"""

# Create your tests here.
class SignUpFormTest(TestCase):
    """
    Tests for the user registration form
    """

    def testValidPassword(self):
        """
        Checks if a user can sign up using a valid password
        """
        form = SignUpForm(data={"username":'testUser', "email":"testEmail@email.com", "password1":"ekozumi###3474t", "password2":"ekozumi###3474t"})
        self.assertTrue(form.is_valid())

    def testInvalidPassword(self):
        """
        Checks that the form rejects invalid passwords
        """
        form = SignUpForm(data={"username":'testUser', "email":"testEmail@email.com", "password1":"password", "password2":"password"})
        self.assertFalse(form.is_valid())

    def testDuplicateUsers(self):
        """
        Checks that two users cant be created with the same username
        """
        form = SignUpForm(data={"username":'testUser', "email":"testEmail@email.com", "password1":"ekozumi###3474t", "password2":"ekozumi###3474t"})
        form.save()
        form2 = SignUpForm(data={"username":'testUser', "email":"testEmail@email.com", "password1":"ekozumi###3474t", "password2":"ekozumi###3474t"})
        self.assertFalse(form2.is_valid())
    
    def testEmptyUsernameField(self):
        """
        Checks that a username is required
        """
        form = SignUpForm(data={"username":'', "email":"testEmail@email.com", "password1":"ekozumi###3474t", "password2":"ekozumi###3474t"})
        self.assertFalse(form.is_valid())

    def testEmptyEmailField(self):
        """
        Checks that a email is required
        """
        form = SignUpForm(data={"username":'testUser', "email":"", "password1":"ekozumi###3474t", "password2":"ekozumi###3474t"})
        self.assertFalse(form.is_valid())

    def testEmptyPasswordField(self):
        """
        Checks that a password is required
        """
        form = SignUpForm(data={"username":'testUser', "email":"testEmail@email.com", "password1":"", "password2":""})
        self.assertFalse(form.is_valid())

class ZumiCreationTest(TestCase):
    """
    Tests the zumi creation form
    """

    def testValidZumi(self):
        """
        Checks if a user can create a pet
        """
        form = ZumiCreationForm(data={"petName":'testPet', "petType":"HEDGEHOG"})
        self.assertTrue(form.is_valid())

    def testInvalidZumi(self):
        """
        Checks if pet does not have a name it cannot be created
        """
        form = ZumiCreationForm(data={"petName":'', "petType":"HEDGEHOG"})
        self.assertFalse(form.is_valid())


class ZumiFeedTest(TestCase):
    """
    Tests that the zumi has been fed
    """

    def setUp(self):
        """
        Forces user to be logged in, as some pages will force redirect user
        if not logged in, also creates a pet for the user
        """
        # User form
        form = SignUpForm(data={"username":'testUser', "email":"testEmail@email.com", "password1":"ekozumi###3474t", "password2":"ekozumi###3474t"})
        user = form.save()

        # Creates a new pet
        pet = Pet(petName = 'petTest', petType = 'Hedgehog')
        pet.save()
        # Links pet and user
        user.profile.petID=pet


class ViewResponseTest(TestCase):
    """
    Checks the HTTP response of webpages
    """

    def setUp(self):
        """
        Forces user to be logged in, as some pages will force redirect user
        if not logged in, also creates a pet for the user
        """
        # User form
        form = SignUpForm(data={"username":'testUser', "email":"testEmail@email.com", "password1":"ekozumi###3474t", "password2":"ekozumi###3474t"})
        user = form.save()

        # Creates a new pet
        pet = Pet(petName = 'petTest', petType = 'Hedgehog')
        pet.save()
        # Links pet and user
        user.profile.petID=pet

        self.client.force_login(user)

    def testLoginView(self):
        """
        Tests the login view
        """
        response = self.client.get('/ekozumi/')
        self.assertEqual(response.status_code, 200)
    
    def testRegistrationView(self):
        """
        test the register view
        """
        response = self.client.get('/ekozumi/register/')
        self.assertEqual(response.status_code, 200)

    def testCharacterCreationView(self):
        """
        test the character creation view
        """

        response = self.client.get('/ekozumi/zumi_creation/')
        self.assertEqual(response.status_code, 200)

    def testHomeView(self):
        """
        test the home view
        """
        response = self.client.get('/ekozumi/home/')
        self.assertEqual(response.status_code, 200)

    def testPuzzleView(self):
        """
        test the puzzle view
        """
        response = self.client.get('/ekozumi/puzzle/')
        self.assertEqual(response.status_code, 200)

    def testMapView(self):
        """
        test the map view
        """
        response = self.client.get('/ekozumi/map/')
        self.assertEqual(response.status_code, 200)

    def testFightIntroView(self):
        """
        test the fight intro page
        """
        response = self.client.post(reverse('intro'), {}, HTTP_REFERER='http://127.0.0.1:8000/ekozumi/map/')
        self.assertEqual(response.status_code, 200)
    
    def testFightView(self):
        """
        test the fight page
        """
        response = self.client.post(reverse('fight'), {}, HTTP_REFERER='http://127.0.0.1:8000/ekozumi/fight_intro/')
        self.assertEqual(response.status_code, 200)
    
    def testFightOutroView(self):
        """
        test the fight outro page
        """
        response = self.client.post(reverse('outro'), {}, HTTP_REFERER='http://127.0.0.1:8000/ekozumi/fight/')
        self.assertEqual(response.status_code, 200)
    
