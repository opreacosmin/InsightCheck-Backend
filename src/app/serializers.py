from rest_framework import serializers
from .models import User, Card, Limit


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        #fields = ['username', 'first_name', 'last_name', 'email', 'password'] #'__all__'

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        #fields = ['card_number', 'type', 'money', 'currency'] #'__all__'
        fields = '__all__'

class LimitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Limit
        #fields = ['amount', 'currency', 'period_start', 'period_end', 'target_date']
        fields = '__all__'