import graphene

import links.schema
import mytest.schema



class Query(mytest.schema.Query, graphene.ObjectType):
    pass

class Mutation(mytest.schema.Mutation, graphene.ObjectType):
    pass

# class Query(links.schema.Query, graphene.ObjectType):
#     pass

# class Mutation(links.schema.Mutation, graphene.ObjectType):
#     pass


schema = graphene.Schema(query=Query, mutation=Mutation)