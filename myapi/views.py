from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


from rest_framework import viewsets
from rest_framework import permissions

from .serializers import ObjetSerializer
from .models import Objet
from .serializers import UserSerializer
from .models import User
from .serializers import CategorySerializer
from .models import Category

class ObjetViewSet(viewsets.ModelViewSet):
    queryset = Objet.objects.all().order_by('name')
    serializer_class = ObjetSerializer
    permission_classes = [permissions.IsAuthenticated]

    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


