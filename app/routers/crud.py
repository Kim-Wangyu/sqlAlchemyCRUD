from app.models.user import users
from app.config.db import conn, session
from fastapi import APIRouter
from app.schemas.user import User




user_router=APIRouter()

test = users(1,'q','w','e')
@user_router.get('/select')
def fetch_all():
    return session.query(users).all()
    # return conn.execute(users.select()).fetchall()

@user_router.post('/insert')
def create_user(id:int,name:str,email:str,password:str):
    session.add(users(id,name,email,password))
    session.commit()
    
    # conn.execute(users.insert().values(name=user.name,email=user.email,password=user.password))
    # return conn.execute(users.select()).fetchall()

@user_router.put('/update/{id}')
def update_user(id:int):
    udt = session.query(users).filter(users.id==1).update({"name":"updataName"})
    print(udt)
    session.commit()

    # conn.execute(users.update().values(name=user.name,email=user.email,password=user.password).where(user.id==id))
    # return conn.execute(users.select().where(users.c.id==id)).first()

@user_router.delete('/delete/{id}')
def delete_user(id:int):
    session.query(users).filter(users.id==1).delete()
    session.commit()
    # conn.execute(users.delete().where(users.c.id==id))
    # return conn.execute(users.select().where(users.c.id==id)).first()