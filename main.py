
import requests

from db import models, films


URL = 'https://cinematica.kg/api/v1/movies/today'

def get_response_to_json(url):
    response = requests.get(url).json()
    return response


json_response = get_response_to_json(URL)['list']
film1 = json_response[0].get('details')

class Film:


    def __init__(self, *args,**kwargs):
        self.__dict__.update(kwargs)


    def get_info(self):
        return self.__dict__

all_films = [Film(**film) for film in film1]
def create_film():

    for film in all_films:
        try:
            print(films.FlimModel.create(**film.get_info()))
        except Exception:
            print(film.get_info())
        continue


def get_films(sort: str =None):# select * from flimmodel
    if sort is None:
        for film in films.FlimModel.select():
           return film.id, film.title, film.value, film.order 

    else:
        if sort == 'title':
            for film in films.FlimModel.select().order_by(films.FlimModel.title):
                print(film.id, film.title, film.value, film.order)
        else:
            raise ValueError("Eror нету такого поля")


def get_film(pk:int): # select * from flimmodel where id == pk 

    film = films.FlimModel.get(films.FlimModel.id==pk)
    return {'id': film.id, 'title':film.title, 'vlaue':film.value} 


def delete_film(pk: int):
    try:
        film = films.FlimModel.get(films.FlimModel.id==pk)
    except Exception:
        print(f'Object how to id {pk} DoesNotExist')
    else:
        return film.delete_instance()

def update_film(pk: int, **kwargs):
    film = films.FlimModel.get(films.FlimModel.id==pk)
    film.title = kwargs.get("title", film.title)
    film.order = kwargs.get("order", film.order)
    film.value = kwargs.get("value", film.value)# ленивый запрос
    film.save()

get_films(sort='title')
update_film(pk=3, title='new _test', order=3)
get_films()
# delete_film(pk=2)
# print(get_films())

# obj1 = Film(**film1[1])

# film_model1 = films.FlimModel(order=obj1.order,
#  value=obj1.value,
#  title=obj1.title)
# film_model1.order = 23
# film_model1.save()
# films.FlimModel.create(order=3, value='test3', title='test3')


# print(obj1.get_info())
# print(obj1.order)
# print(obj1.value)
# print(obj1.title)

#CRUD create read update delete

# models.create_table()



