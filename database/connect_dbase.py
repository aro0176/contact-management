import psycopg2

connect = None
try:
    connect = psycopg2.connect(
        host = "localhost",
        dbname = "contact",
        user = "l3eni",
        password = 123456789,
        port = 5432
    )
except Exception as error :
    print(error)
