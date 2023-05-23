from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URI = 'postgresql://postgres:admin@localhost:5432/agenda'
# DATABASE_URI = 'postgres://angel:NOH6KYGp8sqb4s6bLRLY4QlD9xS49b7q@dpg-chhujn2k728p863o4ukg-a.oregon-postgres.render.com/curso_db_udemy'

def conectar():
    engine = create_engine(DATABASE_URI)
    Session = sessionmaker(bind=engine)
    s = Session()

    if s != None:
        print('Conectado a la BBDD')
    else:
        print('Hubo un error al conectarse a la BBDD')

    return s