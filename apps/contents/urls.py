from django.urls import path

from apps.contents.models import Document, Folder

from apps.contents.views import (
    DocumentListCreateAPIView,
    DocumentRetrieveUpdateDestroyAPIView,

    FolderListCreateAPIView, 
    FolderRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path('documents/', DocumentListCreateAPIView.as_view(), name='document-list-create'),
    path('documents/<int:pk>/', DocumentRetrieveUpdateDestroyAPIView.as_view(), name='document-retrieve-update-destroy'),

    path('folders/', FolderListCreateAPIView.as_view(), name='folder-list-create'),
    path('folders/<int:pk>/', FolderRetrieveUpdateDestroyAPIView.as_view(), name='folder-retrieve-update-destroy'),
]

