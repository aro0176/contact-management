

create_table = '''CREATE TABLE IF NOT EXISTS repertoire(
        id  SERIAL PRIMARY KEY,
        name    varchar(100) NOT NULL,
        phone_number    INT NOT NULL,
        email   varchar(100) NOT NULL
    )'''
