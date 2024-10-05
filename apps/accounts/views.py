from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from apps.accounts.models import CustomUser, Address, Phone
from apps.accounts.serializers import CustomUserSerializer, AddressSerializer, PhoneSerializer



class CreateTokenView(APIView):
    permission_classes = [AllowAny]  # Доступ разрешён для всех

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        # Аутентификация пользователя
        user = authenticate(username=username, password=password)
        if user:
            # Получение или создание токена
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Неверные учетные данные'}, status=status.HTTP_400_BAD_REQUEST)




class CustomUserListCreateAPIView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CustomUserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AddressListCreateAPIView(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class AddressRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated]


class PhoneListCreateAPIView(generics.ListCreateAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer
    permission_classes = [permissions.IsAuthenticated]


class PhoneRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer
    permission_classes = [permissions.IsAuthenticated]
