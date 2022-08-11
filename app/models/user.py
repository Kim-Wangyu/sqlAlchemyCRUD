from sqlalchemy import Column,Table,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from app.config.db import meta,DATABASES
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.sqltypes import INTEGER,String

Base = declarative_base()


class users(Base):
    __tablename__='users'
    id = Column(Integer, primary_key=True)
    name = Column(String,)
    email = Column(String)
    password = Column(String)

    def __init__(self, id, name,email, password):
        self.id=id
        self.name=name
        self.email=email
        self.password = password

        
    def __repr__(self):
        return "<Test('$s', '$s')>" % (self.name,self.email,self.password)


# users = Table('users', meta,
#               Column('id', INTEGER(), primary_key=True),
#               Column('name', String(255)),
#               Column('email', String(255)),
#               Column('password', String(255)),
#               )

meta.create_all(DATABASES)


# class User(Base):
#     __tablename__='User'
#     id=Column(Integer,primary_key=True)
#     pw=Column(String,nullable=False)
#     name=Column(String,nullable=False)
#     email=Column(String)

    # def __init__(self,id,pw,name,email):
    #     self.id=id
    #     self.pw=pw
    #     self.name=name
    #     self.email=email

    # def __repr__(self):
    #     return "<Userr('$s','$s','$s')>" % (self.pw,self.name,self.email)


# if __name__=="__main__":
#     Base.metadata.create_all(DATABASES)

#     Session = sessionmaker()
#     Session.configure(bind=DATABASES)
#     session = Session()

#     test = User(2,'t',3)

