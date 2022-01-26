import graphene


class Query(graphene.ObjectType):
    hello = graphene.String()

    # Add something here

    @classmethod
    def resolve_hello(cls, root, info):
        return "Welcome!"

    # Create a resolver for something here
