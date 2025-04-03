from graphene import Schema, Int, String, List, ObjectType


class Query(ObjectType):
    hello = String(name=String(default_value="World"))

    def resolve_hello(self, info, name):
        return 'Hello ' + name


