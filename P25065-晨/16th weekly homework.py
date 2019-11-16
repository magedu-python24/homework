from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

user = 'root'
pwd = 'root'
host = '192.168.42.144'
port = 3306
db = 'test'
engine = create_engine('mysql+pymysql://{}:{}@{}:{}/{}'.format(user,pwd,host,port,db),echo=True)

Base = declarative_base()

class People(Base):
    __tablename__ = 'People'
    id = Column(Integer,primary_key=True,autoincrement=True)
    username = Column(String(64),nullable=False)
    age =Column(Integer)
    sex =Column(String(8),nullable=False)
    def __repr__(self):
        return "{}: {} {} {} {}".format(self.__class__.__name__,self.id,self.username,self.age,self.sex)
Base.metadata.create_all(engine)


s = People(username='tom',age=80,sex='M')
s.username = 'peter'
s.age = 76
s.sex ='M'

s.username = 'kate'
s.age = 69
s.sex ='F'

Session = sessionmaker(bind=engine)
session = Session()
session.add(s)
session.commit()

person = People(username='jerry',age=90,sex='M')

session.add(person)
session.commit()

p = session.query(People).get(3) #修改
p.username = 'John'
p.age=100
p.sex='M'
session.add(p)
session.commit()

try:
    p1 = session.query(People).get(4) #刪除
    session.delete(p1)
    session.commit()
except Exception:
    session.rollback()


people = session.query(People).limit(6).offset(4) #分頁
print(list(people))


