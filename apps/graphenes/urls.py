from graphene_django.views import GraphQLView

from django.contrib.auth.decorators import login_required
from django.urls import path

from apps.graphenes.schemas import schema


@login_required(login_url='admin')
def graphql_view(request):
    view = GraphQLView.as_view(graphiql=True, schema=schema)
    return view(request)

urlpatterns = [
    path("", graphql_view, name="graphene"),
]
