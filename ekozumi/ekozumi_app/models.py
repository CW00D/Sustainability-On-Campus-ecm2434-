from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Pet(models.Model):
    petID = models.IntegerField(primary_key=True)
    petName = models.CharField(max_length=50)
    lastFed = models.DateTimeField(max_length=100)
    def __str__(self):
        return self.petName

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    petID = models.ForeignKey(Pet, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username

class AdminUser(models.Model):
    userID = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    def __str__(self):
        return self.username

@receiver(post_save, sender = User)
def user_is_created(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user= instance)
    else:
        instance.profile.save()