from django.shortcuts import render
# from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import Card, Profile
from .serializers import CardSerializer
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, AuthenticationFailed

# from .serializers import UserSerializer
# from rest_framework.response import Response
# from rest_framework.exceptions import AuthenticationFailed
# from .models import User
# import jwt, datetime

# Create your views here.

# class RegisterView(APIView):
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)

# class LoginView(APIView):
#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')
#
#         user = User.objects.filter(username=username).first()
#         if user is None:
#             raise AuthenticationFailed('User not found')
#
#         if not user.check_password(password):
#             raise AuthenticationFailed('Incorrect password')
#
#         payload = {
#             'id': user.id,
#             'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=15),
#             'iat': datetime.datetime.utcnow(),
#         }
#
#         # token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256').decode('utf-8')
#         token = jwt.encode(payload, 'secret', algorithm='HS256')
#
#         response = Response()
#         response.set_cookie(key='jwt', value=token, httponly=True)
#         response.data = {
#             'jwt': token,
#         }
#         return response

class getCardsView(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            try:
                profile = Profile.objects.get(userID=user)
                # cards = Card.objects.filter(profileID=profile)
                # serializer = CardSerializer(cards, many=True)
            except:
                raise AuthenticationFailed('Authentication failed')

            cards = Card.objects.filter(profileID=profile)
            serializer = CardSerializer(cards, many=True)

            return Response(serializer.data)
