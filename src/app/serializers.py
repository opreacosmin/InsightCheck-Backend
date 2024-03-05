from rest_framework import serializers
from .models import User, Card

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password'] #'__all__'

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['card_number', 'type', 'money', 'currency'] #'__all__'