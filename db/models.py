from db import films, base

def create_table():
    print("conect database")
    base.db.connect()
    base.db.create_tables([films.FlimModel])


