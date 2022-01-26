import graphene
from schema.types import Property


class Query(graphene.ObjectType):
    hello = graphene.String()

    @classmethod
    def resolve_hello(cls, root, info):
        return "Welcome!"
