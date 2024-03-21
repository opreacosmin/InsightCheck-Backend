from django.shortcuts import render
from rest_framework.views import APIView
from .models import Card, Profile, Limit, LimitType
from .serializers import CardSerializer, LimitSerializer
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, AuthenticationFailed
from rest_framework import status

# Create your views here.

class CardsView(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        try:
            profile = Profile.objects.get(userID=user)
        except Profile.DoesNotExist:
            raise AuthenticationFailed('Authentication failed')

        try:
            cards = Card.objects.filter(profileID=profile)
        except Card.DoesNotExist:
            raise NotFound('Card not found')

        serializer = CardSerializer(cards, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        user = request.user
        try:
            profile = Profile.objects.get(userID=user)
        except Profile.DoesNotExist:
            raise AuthenticationFailed('Authentication failed')

        serializer = CardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(profileID=profile)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # ???

class OneCardView(APIView):
    def get(self, request, card_id):
        user = request.user
        try:
            profile = Profile.objects.get(userID=user)
        except Profile.DoesNotExist:
            raise AuthenticationFailed('Authentication failed')

        try:
            card = Card.objects.get(profileID=profile, id=card_id)
        except Card.DoesNotExist:
            raise NotFound('Card not found')

        serializer = CardSerializer(card)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, card_id):
        user = request.user
        try:
            profile = Profile.objects.get(userID=user)
        except Profile.DoesNotExist:
            raise AuthenticationFailed('Authentication failed')

        try:
            card = Card.objects.get(profileID=profile, id=card_id)
        except Card.DoesNotExist:
            raise NotFound('Card not found')

        card.delete()
        return Response({"detail": "Card deleted successfully"}, status=status.HTTP_200_OK)

class LimitsView(APIView):
    def get(self, request):
        user = request.user
        try:
            profile = Profile.objects.get(userID=user)
        except Profile.DoesNotExist:
            raise AuthenticationFailed('Authentication failed')

        try:
            limits = Limit.objects.filter(profileID=profile)
        except Limit.DoesNotExist:
            raise NotFound('Limit not found')

        serializer = LimitSerializer(limits, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        user = request.user
        try:
            profile = Profile.objects.get(userID=user)
        except Profile.DoesNotExist:
            raise AuthenticationFailed('Authentication failed')

        serializer = LimitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(profileID=profile)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OneLimitView(APIView):
    def get(self, request, limit_id):
        user = request.user
        try:
            profile = Profile.objects.get(userID=user)
        except Profile.DoesNotExist:
            raise AuthenticationFailed('Authentication failed')

        try:
            limit = Limit.objects.get(profileID=profile, id=limit_id)
        except Limit.DoesNotExist:
            raise NotFound('Limit not found')

        serializer = LimitSerializer(limit)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, limit_id):
        user = request.user
        try:
            profile = Profile.objects.get(userID=user)
        except Profile.DoesNotExist:
            raise AuthenticationFailed('Authentication failed')

        try:
            limit = Limit.objects.get(profileID=profile, id=limit_id)
        except Limit.DoesNotExist:
            raise NotFound('Limit not found')

        limit.delete()
        return Response({"detail": "Limit deleted successfully"}, status=status.HTTP_200_OK)

    def put(self, request, limit_id):
        user = request.user
        try:
            profile = Profile.objects.get(userID=user)
        except Profile.DoesNotExist:
            raise AuthenticationFailed('Authentication failed')

        try:
            limit = Limit.objects.get(profileID=profile, id=limit_id)
        except Limit.DoesNotExist:
            raise NotFound('Limit not found')

        serializer = LimitSerializer(limit, data=request.data)
        if serializer.is_valid():
            serializer.save(profileID=profile)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
