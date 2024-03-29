from peewee import *
import datetime

db = PostgresqlDatabase('bookmark',
                        user='postgres',
                        password='',
                        host='localhost',
                        port=5432)

db.connect()


class BaseModel(Model):
    class Meta:
        database = db


class Bookmark(BaseModel):
    title = CharField(unique=True)
    link = CharField(unique=True)
    details = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)


db.create_table([Bookmark])

# test query
# codepip = Bookmark(
#     title='Codepip',
#     link='https://codepip.com/games/',
#     details='Web development games! Learn to code by playing games',
#     )
# codepip.save()
