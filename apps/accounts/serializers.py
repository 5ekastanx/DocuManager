from rest_framework import serializers

from apps.accounts.models import CustomUser, Address, Phone

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only = True)
    class Meta:
        model = Address
        fields = '__all__'


class PhoneSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only = True)
    class Meta:
        model = Phone
        fields = '__all__'

