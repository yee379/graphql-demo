from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import (
    FloatField,
    IntField,
    DictField,
    MapField,
    StringField,
    EmailField,
    ListField,
    URLField,
    ObjectIdField,
    EmbeddedDocumentField,
)


class UserProps(EmbeddedDocument):
    one = FloatField()
    two = FloatField()


class User(Document):
    meta = { 'collection': 'user' }
    ID = ObjectIdField()
    uid = StringField(required=True)
    uid_number = IntField(required=True)
    eppns = ListField( EmailField() )
    props = EmbeddedDocumentField(UserProps)


class Facility(Document):
    meta = {"collection": "facility"}
    ID = ObjectIdField()
    name = StringField()
    description = StringField()


class Repo(Document):
    meta = {"collection": "repo"}
    ID = ObjectIdField()
    name = StringField(required=True)
    facility = StringField() # shoudl probably ref faciilty
    description = StringField()
    gid = IntField(required=True)
    principal = StringField() # should probably be a ref to a User
    leaders = ListField( StringField() )
    users = ListField( StringField() )
    

