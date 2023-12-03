from mongoengine import Document, ListField, StringField, URLField # type: ignore
from mongoengine.fields import IntField # type: ignore


class DBCategory(Document):
    id = IntField()
