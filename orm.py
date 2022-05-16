import psycopg2


connection = psycopg2.connect(
    database='users',
    user='postgres',
    password='',
    host='lovalhost',
    port='5432'
)

print('Database succeful opened')