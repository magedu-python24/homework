#### 名词解释：主键、外键、索引、事务、存储过程和触发器分别是什么？

主键：表中由一列或多列组中的唯一值，用来确定记录的唯一性，不可以为空或null。

外键：一张表的某一字段，关联了另一张表的主键，那这个字段就称之为外键。

索引：对一列或多列字段设定索引，将显著的提高查询速度，空间换时间的。

事务：由若干条语句组成完成一系列动作，其中任何一步失败，所有操作都撤销，必须支持ACID（Atomicity, Consistency, Isolation, Durability）四个属性。

存储过程：一段可以被传参调用的sql语句，用来完成特定功能。

触发器：由事件触发的特殊存储过程。

#### 使用SQLAlchemy定义一个包含username、age、sex字段的表

#### 写出使用SQLAlchemy操作上述表CRUD例子

#### 实现查询的分页的思路

```python
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = sqlalchemy.create_engine('mysql+pymysql://lucas:iloveliya@192.168.28.128/class', echo=True)
Base = declarative_base()


class Student(Base):
    __tablename__ = 'student'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(60))
    age = sqlalchemy.Column(sqlalchemy.Integer)
    sex = sqlalchemy.Column(sqlalchemy.Enum('F', 'M'))

    def __repr__(self):
        return "<Student(name='%s', age='%d', sex='%s')>" % (
            self.name, self.age, self.sex
        )


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
# add
t = Student(name='lucas')
t.age = 28
t.sex = 'M'
session.add(t)
session.commit()
# query
student = session.query(Student).get(1)
print(student)
# update
student.name = 'lucas cheng'
student.age = 27
session.add(student)
session.commit()

# delete
del_stu = session.query(Student).get(1)
try:
    session.delete(del_stu)
    session.flush()
    session.commit()
except Exception as e:
    session.rollback()
    print('action failed')
    print(e)


def out(pageinfo):
    for i in pageinfo:
        print(i)


pageinfo = session.query(Student).limit(2).offset(0)
out(pageinfo)
pageinfo = session.query(Student).limit(2).offset(2)
out(pageinfo)

```



#### 



#### 

