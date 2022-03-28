from graphene import relay
from graphene_mongo import MongoengineObjectType
from .models import UserProps, User, Repo, Facility

class UserPropsType(MongoengineObjectType):
    class Meta:
        model = UserProps

class UserType(MongoengineObjectType):
    class Meta:
        model = User

class RepoType(MongoengineObjectType):
    class Meta:
        model = Repo
        #interfaces = (relay.Node,)

class FacilityType(MongoengineObjectType):
    class Meta:
        model = Facility
