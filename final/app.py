from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func

from database import SessionLocal
from schema import PostGet,UserGet, FeedGet
from table_user import User
from table_post import Post
from table_feed import Feed

app=FastAPI()


def get_db():
    with SessionLocal() as db:
        return db

@app.get("/user/{id}", response_model=UserGet)
def get_user(id:int , db: Session = Depends(get_db)):
    final = db.query(User).filter(User.id==id).one_or_none()
    if not final:
        raise HTTPException(status_code=404, detail="User not found")
    return final



@app.get("/post/{id}", response_model=PostGet)
def get_post(id:int , db: Session=Depends(get_db)):
    res = db.query(Post).filter(Post.id==id).one_or_none()
    if not res:
        raise HTTPException(status_code=404, detail="User not found")
    return res

@app.get("/user/{id}/feed", response_model=List[FeedGet])
def get_feed(id:int, limit: int = 10, db: Session=Depends(get_db) ):
    req = db.query(Feed).filter(Feed.user_id==id).order_by(Feed.time.desc()).limit(limit).all()
    if not req:
        raise HTTPException(status_code=200, detail=[])
    return req


@app.get("/post/{id}/feed", response_model=List[FeedGet])
def get_feed(id:int, limit: int = 10, db: Session=Depends(get_db) ):
    req = db.query(Feed).filter(Feed.post_id==id).order_by(Feed.time.desc()).limit(limit).all()
    if not req:
        raise HTTPException(status_code=200, detail=[])
    return req

@app.get("/post/recommendations/", response_model=List[PostGet])
def like( limit:int=10, db: Session=Depends(get_db)):
    result = (
        db.query(Post.id, Post.text, Post.topic,func.count(Feed.action).label("like_count"))
              .join(Feed, Feed.post_id == Post.id)
              .filter(Feed.action=="like")
              .group_by(Post.id,Post.text,Post.topic)
              .order_by(func.count(Feed.action).desc())
              .limit(limit)
              .all()
              )
    return result

