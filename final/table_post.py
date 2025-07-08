from database import Base
from sqlalchemy import Column, Integer, String
from database import SessionLocal

class Post(Base):
    __tablename__ = "post"
    #__table_args__ = {"schema": "cd"}
    id = Column(Integer, primary_key=True)
    text = Column(String)
    topic = Column(String)

# отбераем все посты с topic = "business", сортируем их по убыванию их id и печатаем первые 10 id списком
if __name__ == "__main__":
    session = SessionLocal()
    res = []
    for x in (
            session.query(Post)
                    .filter(Post.topic=="business")
                    .order_by(Post.id.desc())
                    .limit(10)
                    .all()
    ):
        res.append(x.id)
    print(res)