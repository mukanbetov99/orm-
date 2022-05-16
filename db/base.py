from peewee import PostgresqlDatabase, Model

db = PostgresqlDatabase(
'snake_film',
 user='postgres',
 password='1',
 host='localhost',
 port='5432'
 )

class BaseModel(Model):

    class Meta:
        database = db

