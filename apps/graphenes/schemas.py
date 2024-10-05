import graphene

from apps.graphenes.queries import Query


schema = graphene.Schema(query=Query)
