from db import conectar
from models import Contacto, Pertenece


def seleccionar_contactos(id_usuario, campo, orden):
    try:
        session = conectar()

        if campo == 'ID' and orden == 'ASC':
            contactos = session.query(Contacto).join(Pertenece, Contacto.id == Pertenece.id_contacto).filter(Pertenece.id_usuario == id_usuario).order_by(Contacto.id).all()
        elif campo == 'ID' and orden == 'DESC':
            contactos = session.query(Contacto).join(Pertenece, Contacto.id == Pertenece.id_contacto).filter(Pertenece.id_usuario == id_usuario).order_by(Contacto.id.desc()).all()
        elif campo == 'NOMBRE' and orden == 'ASC':
            contactos = session.query(Contacto).join(Pertenece, Contacto.id == Pertenece.id_contacto).filter(Pertenece.id_usuario == id_usuario).order_by(Contacto.nombre).all()
        elif campo == 'NOMBRE' and orden == 'DESC':
            contactos = session.query(Contacto).join(Pertenece, Contacto.id == Pertenece.id_contacto).filter(Pertenece.id_usuario == id_usuario).order_by(Contacto.nombre.desc()).all()

        return contactos
    
    except Exception as e:
        print(e)
        return 'Se ha producido un error.'
    
    finally:
        session.close()



def seleccionar_contacto(id):
    try:
        session = conectar()
        contacto = session.query(Contacto).filter(Contacto.id == id).all()[0]

        return contacto
        
    except Exception as e:
        print(f'Ha ocurrido el siguiente error: {e}')

        return e

    finally:
        session.close()



def busqueda_contactos(id_usuario, value):
    try:
        session = conectar()
        contactos = session.query(Contacto).join(Pertenece, Contacto.id == Pertenece.id_contacto).filter(Pertenece.id_usuario == id_usuario).filter((Contacto.nombre.ilike('%'+value+'%')) | (Contacto.apellidos.ilike('%'+value+'%')) | (Contacto.email.ilike('%'+value+'%')) | (Contacto.direccion.ilike('%'+value+'%'))).order_by(Contacto.nombre).all()

        return contactos
    
    except Exception as e:
        print(f'Ha ocurrido el siguiente error: {e}')

        return e
    
    finally:
        session.close()




def insertar_contacto(id_usuario, nombre, apellidos, direccion, email, telefono):
    try:
        contacto = Contacto(
            nombre=nombre,
            apellidos=apellidos,
            direccion=direccion,
            email=email,
            telefono=telefono
        )
        session = conectar()
        session.add(contacto)
        session.commit()

        session.refresh(contacto)
        id_contacto = contacto.id

        pertenece = Pertenece(
            id_usuario=id_usuario,
            id_contacto=id_contacto
        )

        session.add(pertenece)
        session.commit()

        return True

    except Exception as e:
        print(e)
        return False
    finally:
        session.close()


def actualizar_contacto(id,nombre, apellidos,direccion,email,telefono):
    try:
        session = conectar()
        contacto = session.query(Contacto).get(id)
        contacto.nombre = nombre
        contacto.apellidos = apellidos
        contacto.direccion = direccion
        contacto.email = email
        contacto.telefono = telefono

        session.add(contacto)
        session.commit()

        return True
    
    except Exception as e:
        print(e)
        return False

    finally:
        session.close()


def eliminar_contacto(id_usuario, id_contacto):
    try:
        session = conectar()
        session.query(Pertenece).filter(Pertenece.id_contacto == id_contacto).filter(Pertenece.id_usuario == id_usuario).delete()
        contacto = session.query(Contacto).get(id_contacto)
        session.delete(contacto)

        session.commit()
        return True

    except Exception as e:
        print(e)
        return False
    finally:
        session.close()