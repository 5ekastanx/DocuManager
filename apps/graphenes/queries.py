import graphene
from apps.graphenes.modeltypes.types_obg import (
    UserType,
    AddressType,
    PhoneType,
    FolderType,
    DocumentType,
)

from apps.accounts.models import (
    CustomUser,
    Address,
    Phone,
)

from apps.contents.models import (
    Folder,
    Document,
)


class Query(graphene.ObjectType):
    user_model = graphene.List(UserType)
    user_model_by_id = graphene.Field(UserType, id=graphene.Int(required=True))

    address_model = graphene.List(AddressType)
    address_model_by_id = graphene.Field(
        AddressType, id=graphene.Int(required=True))

    phone_model = graphene.List(PhoneType)
    phone_model_by_id = graphene.Field(
        PhoneType, id=graphene.Int(required=True))

    folder_model = graphene.List(FolderType)
    folder_model_by_id = graphene.Field(
        FolderType, id=graphene.Int(required=True))

    document_model = graphene.List(DocumentType)
    document_model_by_id = graphene.Field(
        DocumentType, id=graphene.Int(required=True))

    def resolve_user_model(self, info):
        return CustomUser.objects.all()

    def resolve_user_model_by_id(self, info, id):
        return CustomUser.objects.get(id=id)

    def resolve_address_model(self, info):
        return Address.objects.all()

    def resolve_address_model_by_id(self, info, id):
        return Address.objects.get(id=id)

    def resolve_phone_model(self, info):
        return Phone.objects.all()

    def resolve_phone_model_by_id(self, info, id):
        return Phone.objects.get(id=id)

    def resolve_folder_model(self, info):
        return Folder.objects.all()

    def resolve_folder_model_by_id(self, info, id):
        return Folder.objects.get(id=id)

    def resolve_document_model(self, info):
        return Document.objects.all()

    def resolve_document_model_by_id(self, info, id):
        return Document.objects.get(id=id)
