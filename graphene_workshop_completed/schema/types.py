import graphene


class Amenity(graphene.Enum):
    RESERVED_PARKING = "RESERVED_PARKING"
    EV_PARKING = "EV_PARKING"


class Unit(graphene.ObjectType):
    id = graphene.String(required=True)
    squareFeet = graphene.Int(required=True)
    bedrooms = graphene.Int(required=True)
    amenity = graphene.List(Amenity)


class Property(graphene.ObjectType):
    id = graphene.String(required=True)
    name = graphene.String(required=True)
    address = graphene.String(required=True)
    units = graphene.List(Unit)


class LeasingAgent(graphene.ObjectType):
    name = graphene.String(required=True)
    email = graphene.String(required=True)
