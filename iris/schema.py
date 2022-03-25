from graphene import ObjectType, Schema, List, Field
from graphene.relay import Node
from graphene_mongo.fields import MongoengineConnectionField
from .models import User,Repo,Facility
from .types import UserType, RepoType, FacilityType
from .mutations import (
        RepoInput, CreateRepoMutation, UpdateRepoMutation, DeleteRepoMutation,
        UserInput, CreateUserMutation, UpdateUserMutation,
        FacilityInput, CreateFacilityMutation
)

import logging

class Mutations(ObjectType):
    create_repo = CreateRepoMutation.Field()
    update_repo = UpdateRepoMutation.Field()
    delete_repo = DeleteRepoMutation.Field()

    create_user = CreateUserMutation.Field()
    update_user = UpdateUserMutation.Field()

    create_facility = CreateFacilityMutation.Field()

class Query(ObjectType):
    node = Node.Field()
    repos = List( RepoType, filters=RepoInput() )
    facilities = List(FacilityType, filters=FacilityInput() )
    users = List(UserType, filters=UserInput() )

    def resolve_repos(self, info, **kwargs):
        return Repo.objects(**kwargs.get("filters", {})) 
    def resolve_facilities(self, info, **kwargs):
        return Facility.objects(**kwargs.get("filters",{}))
    def resolve_users(self, info):
        return User.objects(**kwargs.get("filters",{}))



