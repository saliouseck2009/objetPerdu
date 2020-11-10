# serializers.py

from rest_framework import serializers
from .models import *

class ObjetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Objet
        fields = '__all__'

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        field = '__all__'
