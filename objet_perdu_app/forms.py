from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core import mail

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=150, help_text='Email')


    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2', )

  



"""
class SignUpForm(UserCreationForm):
    # username = forms.CharField(label="Nom d'utilisateur",
    #                            widget=forms.TextInput(
    #                                attrs={
    #                                    "class": "form-control"
    #                                }
    #                            ))
    username = forms.CharField()

    # phone = forms.TextInput(label="Numéro de Téléphone",
    #                         widget=forms.TextInput(
    #                             attrs={
    #                                 "class":"form-control"
    #                             }
    #                         ))
    phone = forms.TextInput()

    # email = forms.EmailField(label="Email",
    #                          widget=forms.EmailInput(
    #                                attrs={
    #                                    "class":"form-control"
    #                                }
    #                          ))
    email = forms.EmailField()
    # password1 = forms.PasswordInput(label="Mot de Passe",
    #                                 widget=forms.PasswordInput(
    #                                     attrs={
    #                                         "class":"form-control"
    #                                     }
    #                                 ))
    password1 = forms.PasswordInput()
    # password2 = forms.PasswordInput(label="Retaper le mot de passe",
    #                                 widget=forms.PasswordInput(
    #                                     attrs={
    #                                         "class":"form-control"
    #                                     }
    #                                 ))
    password2 = forms.PasswordInput()
"""


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
