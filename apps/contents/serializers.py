from rest_framework import serializers

from apps.contents.models import Document, Folder
from apps.accounts.serializers import CustomUserSerializer

class FolderSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)


    class Meta:
        model = Folder
        fields = '__all__'

class DocumentSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)

    class Meta:
        model = Document
        fields = '__all__'



