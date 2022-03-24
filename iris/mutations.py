import graphene as g
from .models import Facility ,Repo, User
from .types import FacilityType, RepoType, UserType


###
# user
###

class UserInput(g.InputObjectType):
    id = g.ID()
    uid = g.String()
    uid_number = g.Int()
    eppns = g.List( g.String )

class CreateUserMutation(g.Mutation):
    user = g.Field(UserType)
    class Arguments:
        data = UserInput(required=True)

    def mutate(self, info, data=None):
        user = User(
                uid=data.uid,
                uid_number=data.uid_number,
                eppns=data.eppns
        )
        user.save()
        return CreateUserMutation(user=user)

class UpdateUserMutation(g.Mutation):
    user = g.Field(UserType)

    class Arguments:
        data = UserInput(required=True)

    @staticmethod
    def get_object(id):
        return User.objects.get(pk=id)

    def mutate(self, info, data=None):
        user = UpdateUserMutation.get_object(data.id)
        for field in ( 'uid', 'eppns', 'uid_number' ):
            if field in data:
                setattr( user, field, getattr( data, field ) )
        user.save()
        return UpdateUserMutation(user=user)

###
# Facility
###

class FacilityInput(g.InputObjectType):
    id = g.ID()
    name = g.String()
   
class CreateFacilityMutation(g.Mutation):
    facility = g.Field(FacilityType)

    class Arguments:
        data = FacilityInput(required=True)

    def mutate(self, info, data=None):
        facility = Facility(
            name=data.name
        )
        facility.save()
        return CreateFacilityMutation(facility=facility)

###
# Repo
###

class RepoInput(g.InputObjectType):
    id = g.ID()
    name = g.String()
    gid = g.Int()
    facility = g.String()
    description = g.String()
    principal = g.String()
    leaders = g.List( g.String )
    users = g.List( g.String )


class CreateRepoMutation(g.Mutation):
    repo = g.Field(RepoType)

    class Arguments:
        data = RepoInput(required=True)

    def mutate(self, info, data=None):
        repo = Repo(
            name=data.name,
            gid=data.gid,
        )
        repo.save()
        return CreateRepoMutation(repo=repo)


class UpdateRepoMutation(g.Mutation):
    repo = g.Field(RepoType)

    class Arguments:
        data = RepoInput(required=True)

    @staticmethod
    def get_object(id):
        return Repo.objects.get(pk=id)

    def mutate(self, info, data=None):
        repo = UpdateRepoMutation.get_object(data.id)
        for field in ( 'name', 'gid', 'description', 'facility', 'principal', 'leaders', 'users' ):
            if field in data:
                setattr( repo, field, getattr( data, field ) )
        repo.save()
        return UpdateRepoMutation(repo=repo)


class DeleteRepoMutation(g.Mutation):
    class Arguments:
        id = g.ID(required=True)

    success = g.Boolean()

    def mutate(self, info, id):
        try:
            Repo.objects.get(pk=id).delete()
            success = True
        except ObjectDoesNotExist:
            success = False

        return DeleteRepoMutation(success=success)

