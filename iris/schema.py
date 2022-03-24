from graphene import ObjectType, Schema, List
from graphene.relay import Node
from graphene_mongo.fields import MongoengineConnectionField
from .models import User,Repo,Facility
from .types import UserType, RepoType, FacilityType
from .mutations import (
        CreateRepoMutation, UpdateRepoMutation, DeleteRepoMutation,
        CreateUserMutation, UpdateUserMutation,
        CreateFacilityMutation
)


class Mutations(ObjectType):
    create_repo = CreateRepoMutation.Field()
    update_repo = UpdateRepoMutation.Field()
    delete_repo = DeleteRepoMutation.Field()

    create_user = CreateUserMutation.Field()
    update_user = UpdateUserMutation.Field()

    create_facility = CreateFacilityMutation.Field()

class Query(ObjectType):
    node = Node.Field()
    repos = List(RepoType) #MongoengineConnectionField(RepoType)
    facilities = List(FacilityType)
    users = List(UserType)

    def resolve_repos(self, info, **kwargs):
        return Repo.objects.all() 
    def resolve_facilities(self, info):
        return Facility.objects.all()
    def resolve_users(self, info):
        return User.objects.all()



