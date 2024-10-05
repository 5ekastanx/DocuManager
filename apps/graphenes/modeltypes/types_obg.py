from graphene_django import DjangoObjectType


from apps.accounts.models import (
    CustomUser,
    Address,
    Phone,
)

from apps.contents.models import (
    Folder,
    Document,
)


class UserType(DjangoObjectType):
    class Meta:
        model = CustomUser


class AddressType(DjangoObjectType):
    class Meta:
        model = Address


class PhoneType(DjangoObjectType):
    class Meta:
        model = Phone


class FolderType(DjangoObjectType):
    class Meta:
        model = Folder


class DocumentType(DjangoObjectType):
    class Meta:
        model = Document
