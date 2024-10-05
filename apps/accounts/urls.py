from django.urls import path
from apps.accounts.views import (
    CustomUserListCreateAPIView,
    CustomUserRetrieveUpdateDestroyAPIView,

    AddressListCreateAPIView,
    AddressRetrieveUpdateDestroyAPIView,
    
    PhoneListCreateAPIView,
    PhoneRetrieveUpdateDestroyAPIView,
)


urlpatterns = [
    path('users/', CustomUserListCreateAPIView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', CustomUserRetrieveUpdateDestroyAPIView.as_view(), name='user-detail'),

    path('addresses/', AddressListCreateAPIView.as_view(), name='address-list-create'),
    path('addresses/<int:pk>/', AddressRetrieveUpdateDestroyAPIView.as_view(), name='address-detail'),
    
    path('phones/', PhoneListCreateAPIView.as_view(), name='phone-list-create'),
    path('phones/<int:pk>/', PhoneRetrieveUpdateDestroyAPIView.as_view(), name='phone-detail'),
]
