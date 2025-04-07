from graphene import Schema
from starlette_graphene3 import GraphQLApp, make_graphiql_handler
from .service import Query

schema = Schema(query=Query)
graphql_app = GraphQLApp(schema=schema, on_get=make_graphiql_handler())