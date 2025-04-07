from graphene import Schema
from starlette_graphene3 import GraphQLApp
from .service import Query

schema = Schema(query=Query)
graphql_app = GraphQLApp(schema=schema)