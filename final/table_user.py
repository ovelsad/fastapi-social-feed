from database import Base
from sqlalchemy import Column, Integer, String, func
from database import SessionLocal

class User(Base):
    __tablename__ = "user"
    #__table_args__ = {"schema": "cd"}
    id = Column(Integer, primary_key=True)
    age = Column(Integer)
    city = Column(String)
    country = Column(String)
    exp_group = Column(Integer)
    gender = Column(Integer)
    os = Column(String)
    source = Column(String)

if __name__ == "__main__":
    session = SessionLocal()
    req = (
        session.query(User.country, User.os, func.count().label('count'))
        .filter(User.exp_group==3)
        .group_by(User.country, User.os)
        .having(func.count() > 100)
        .order_by(func.count().desc())
        .all()
    )
    res = []
    for x in req:
        res.append((x.country, x.os, x.count))
    print(res)
