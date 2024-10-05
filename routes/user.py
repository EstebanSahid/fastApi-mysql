from fastapi import APIRouter
from config.db import con
from models.user import users
from schemas.User import User
from cryptography.fernet import Fernet

user = APIRouter()

key = b'WgWx8gKOnJZRjR-QAGzx9drg_XaN94FqZKqUhylItiU='
f = Fernet(key)

@user.get("/users")
def getUsers():
    return con.execute(users.select()).fetchall()

@user.post("/users")
def create_user(user: User):
    pass_cifrada = f.encrypt(user.password.encode())
    add = users.insert().values(
        name = user.name,
        email = user.email,
        password = pass_cifrada
    )
    res = con.execute(add)
    con.commit()
    print(res.lastrowid)
    return "Guardado"


#@user.get("/users")
#def hola():
#    return "Hola u"

#@user.get("/users")
#def hola():
#    return "Hola u"

#@user.get("/users")
#def hola():
#    return "Hola u"