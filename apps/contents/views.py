from django.contrib.auth import authenticate
from django.db.models import Q

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from apps.contents.models import Document, Folder
from apps.contents.serializers import DocumentSerializer, FolderSerializer


class DocumentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def list(self, request, *args, **kwargs):
        user = request.user
        queryset = self.get_queryset().filter(Q(user=user))
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
    

class DocumentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'

    def retrieve(self, request, *args, **kwargs):
        user = request.user
        document: Document = self.get_object()

        if document.user == user or document.access.contains(user):
            return Response(self.serializer_class(document).data)
        else:
            return Response(
                data={"detail": "У вас недостаточно прав для выполнения данного действия."},
                status=status.HTTP_403_FORBIDDEN)

    def update(self, request, *args, **kwargs):
        user = request.user
        document: Document = self.get_object()
        
        if document.user == user:
            return super().update(request, *args, **kwargs)
        else:
            return Response(
                data={"detail": "У вас недостаточно прав для выполнения данного действия."},
                status=status.HTTP_403_FORBIDDEN)
        
    def destroy(self, request, *args, **kwargs):
        user = request.user
        document: Document = self.get_object()

        if document.user == user:
            return super().destroy(request, *args, **kwargs)
        else:
            return Response(
                data={"detail": "У вас недостаточно прав для выполнения данного действия."},
                status=status.HTTP_403_FORBIDDEN)


class FolderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer
    permission_classes = [permissions.IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def list(self, request, *args, **kwargs):
        user = request.user
        queryset = self.get_queryset().filter(Q(user=user))
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class FolderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        user = request.user
        folder: Folder = self.get_object()

        if folder.user == user:
            return Response(self.serializer_class(folder).data)
        else:
            return Response(
                data={"detail": "У вас недостаточно прав для выполнения данного действия."},
                status=status.HTTP_403_FORBIDDEN)
    
    def update(self, request, *args, **kwargs):
        user = request.user
        folder: Folder = self.get_object()

        if folder.user == user:
            return super().update(request, *args, **kwargs)
        else:
            return Response(
                data={"detail": "У вас недостаточно прав для выполнения данного действия."},
                status=status.HTTP_403_FORBIDDEN)
    
    def destroy(self, request, *args, **kwargs):
        user = request.user
        folder: Folder = self.get_object()

        if folder.user == user:
            return super().destroy(request, *args, **kwargs)
        else:
            return Response(
                data={"detail": "У вас недостаточно прав для выполнения данного действия."},
                status=status.HTTP_403_FORBIDDEN)
        