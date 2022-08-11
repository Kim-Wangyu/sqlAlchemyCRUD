from operator import or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


DATABASES= create_engine('sqlite:///sql.db')


Base = declarative_base()

class User(Base):
    __tablename__='test5'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    pw = Column(Integer)

    def __init__(self, id, name, pw):
        self.id=id
        self.name=name
        self.pw = pw

        
    def __repr__(self):
        return "<Test('$s', '$s')>" % (self.name,self.pw)

if __name__=="__main__":
    Base.metadata.create_all(DATABASES)

    Session = sessionmaker()
    Session.configure(bind=DATABASES)
    session = Session()

    test = User(2,'t',3)



##@@@@@@@@@@@@@@@@@@
    # session.add(test)
    # session.commit()

    # DE =session.query(User).filter(User.id==1).delete()
    # print(DE)
    # session.commit()

    # upt = session.query(User).filter(User.id ==1).update({"name":"update this content"})
    # print(upt)
    # session.commit()

    user = session.query(User).filter((test.id==2)).all()
    session.commit()

# Base.metadata.create_all(engine)  #생성
# Base.metadata.drop_all(engine)  #삭제
