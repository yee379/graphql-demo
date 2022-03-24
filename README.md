# simple example of graphql with fastapi and graphene


## initialisation

check out code

    git clone https://github.com/yee379/graphql-demo

create a new virtual env with

    virtualenv graphql-demo
    graphql-demo/bin/pip install -r graphql-demo/requirements.txt
    cd graphql-demo

install mongo and start it with

    mongod --config mongod.conf

then initiate the uvicorn server with

    ./bin/uvicorn main:app  --reload

## use

goto http://localhost:8000/graphql to bring up the graphql browser.

## example queries

get users

```
{ { users { id uid uidNumber eppns }}
```

get repos

```
{ repos { id name description principal leaders users }}
```

add new user

```
mutation{
  createUser ( data: {
    uid: "meme",
    uidNumber: 1670,
    eppns: [ "me@here.com", "you@there.com" ]
  }) {
    user {
      uid eppns uidNumber
    }
  }
}
```

change user data

```
mutation{
  updateUser ( data: {
    id: "623c1c9a7a249e2fb632eaf4",
    uid: "youyou",
    eppns: [ "me@here.com", "you@there.com", "anywhere@here.com" ]
  }) {
    user {
      id uid eppns uidNumber
    }
  }
}
```
