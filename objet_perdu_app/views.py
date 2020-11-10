
from django.contrib.auth import login, authenticate,logout
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_text
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib import messages
from django.urls import reverse
from django.template import TemplateDoesNotExist
from django.contrib.auth.decorators import login_required


from .tokens import account_activation_token
from .forms import SignUpForm, ContactForm

# Create your views here.

@login_required(login_url=' /signin/')
def home_view(request):
    
    return render(request, 'objet_perdu/home.html',{'user':request.user})


def signup_view(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            
            return redirect(reverse('objet_perdu:signin'))
            
    else:
        form = SignUpForm()
    return render(request, 'objet_perdu/signup.html', {'form': form})


def signin_view(request):
    if request.user.is_authenticated:
        print("l'utilisateur s'est connecté"+request.user.username)
        return redirect(reverse('objet_perdu:home'))
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect(reverse('objet_perdu:home'))
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'objet_perdu/signin.html', context)
    
def logoutUser(request):
	logout(request)
	return redirect('login')


"""
def signup_view(request):
    form = SignUpForm(request.POST)
    form.
    print(form.cleaned_data())
    if form.is_valid():
        print(form.cleaned_data())
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        email = form.cleaned_data.get('email')
        phone = form.cleaned_data.get('phone')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'objet_perdu/signup.html', {'form': form})    
"""


# Views for forms


# view for contact form
def contact_view(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['saliouseck2009@gmail.com']
            if cc_myself:
                recipients.append(sender)
            try:
                send_mail(subject, message, sender, recipients)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success_contact')
    return render(request, "objet_perdu/contact.html", {'form': form})


def success_contact(request):
    return render(request, 'objet_perdu/success_contact.html')


"""
def signup_view(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')
    return render(request, 'objet_perdu/signup.html', {'form': form})
"""
"""

    
    
    
    def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('objet_perdu/activation_request.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignUpForm()
    return render(request, 'objet_perdu/signup.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')
"""
