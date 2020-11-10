# myapi/urls.py

from django.urls import include, path
from . import views
from .views import home_view, signup_view, contact_view, success_contact,signin_view

app_name='objet_perdu'

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', home_view, name="home"),
    path('signup/', signup_view, name="signup"),
    path('signin/', signin_view, name="signin"),
    path('contact/', contact_view, name="contact"),
    path('success_contact/', success_contact, name="success_contact"),
    
]

