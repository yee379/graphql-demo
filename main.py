from fastapi import FastAPI

from starlette_graphene3 import GraphQLApp, make_graphiql_handler
import uvicorn

from iris.schema import Query, Mutations
from iris.types import UserType, RepoType, FacilityType

from mongoengine import connect, disconnect
from graphene import Schema

import logging
formatter = uvicorn.logging.DefaultFormatter("%(levelprefix)s %(asctime)s | %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI()

# connect to mongo
@app.on_event("startup")
async def create_db_client():
    connect('new-iris')

@app.on_event("shutdown")
async def shutdown_db_client():
    disconnect()

# build graphql
schema = Schema(query=Query, mutation=Mutations, types=[UserType, RepoType, FacilityType])
app.add_route( "/graphql", GraphQLApp(
    schema=schema,
    on_get=make_graphiql_handler())
)


