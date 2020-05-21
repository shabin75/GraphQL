import graphene
from graphene_django import DjangoObjectType

from .models import Test

class TestType(DjangoObjectType):
    class Meta:
        model = Test


class Query(graphene.ObjectType):
    tests = graphene.List(TestType)

    def resolve_links(self, info, **kwargs):
        return Test.objects.all()


class CreateTest(graphene.Mutation):
    id = graphene.Int()
    age=graphene.Int()
    name = graphene.String()

    #2
    class Arguments:
        age=graphene.String()
        name = graphene.String()

    #3
    def mutate(self, info, age, name):
        test = Test(age=age, name=name)
        test.save()

        return CreateTest(
            id=test.id,
            name=test.name,
            age=test.age )


#4
class Mutation(graphene.ObjectType):
    create_test = CreateTest.Field()