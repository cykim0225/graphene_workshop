import graphene

from schema.types import LeasingAgent


class AddLeasingAgent(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        email = graphene.String(required=True)

    agent = graphene.Field(lambda: LeasingAgent)

    @classmethod
    def mutate(cls, root, info, name, email):
        agent = LeasingAgent(name=name, email=email)
        return AddLeasingAgent(agent=agent)


class Mutation(graphene.ObjectType):
    add_leasing_agent = AddLeasingAgent.Field()
