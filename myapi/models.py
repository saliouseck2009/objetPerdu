from django.db import models
from django.db.models.fields.related import ForeignKey

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
"""
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, null=True, blank=True)
    email = models.CharField(max_length=100)
    signup_confirmation = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
"""
class Objet(models.Model):

    name = models.CharField(
        max_length=64, help_text="Veillez saisir votre nom")
    date = models.DateTimeField(auto_now_add=True)
    location = models.CharField(
        max_length=200, help_text="Veillez renseigner le lieu où vous perdu ou retrouvé l'objet")
    description = models.TextField()
    reward = models.PositiveIntegerField(null=True, blank=True)
    category = ForeignKey(Category, blank=True,
                          null=True, on_delete=models.SET_NULL, verbose_name="catégorie d'un objet")
    user = ForeignKey(User, blank=True,
                      null=True, on_delete=models.SET_NULL, verbose_name="Propriétaire de l'objet")

    def __str__(self):
        return f"{self.name} : \n {self.description}"






