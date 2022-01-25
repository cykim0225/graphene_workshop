import graphene
from flask import Flask
from flask_graphql import GraphQLView

from schema.query import Query
from schema.mutation import Mutation

from healthcheck import healthcheck

schema = graphene.Schema(query=Query, mutation=Mutation)


def init_app():
    app = Flask(__name__)
    app.debug = True
    app.add_url_rule(
        "/graphql",
        view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True),
    )
    app.add_url_rule("/healthcheck", "healthcheck", healthcheck)

    return app


app = init_app()
