from django.contrib import admin
from django.contrib.auth.models import User
from .models import Category
from .models import Objet

# Register your models here.
admin.site.register(Category)
admin.site.register(Objet)