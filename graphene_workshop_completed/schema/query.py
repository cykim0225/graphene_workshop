import graphene
from schema.types import Property, Unit
from data import get_unit_by_id, get_property_by_id


class Query(graphene.ObjectType):
    hello = graphene.String()

    unit_by_id = graphene.Field(Unit, id=graphene.String(required=True))

    property_by_id = graphene.Field(Property, id=graphene.String(required=True))

    @classmethod
    def resolve_hello(cls, root, info):
        return "Welcome!"

    @classmethod
    def resolve_unit_by_id(cls, root, info, id):
        return get_unit_by_id(id)

    @classmethod
    def resolve_property_by_id(cls, root, info, id):
        return get_property_by_id(id)
