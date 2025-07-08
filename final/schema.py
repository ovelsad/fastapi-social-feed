import datetime
from pydantic import BaseModel

class UserGet(BaseModel):
    id: int
    age: int
    city: str
    country: str
    exp_group: int
    gender: int
    os: str
    source: str

    class Config:
        orm_mode = True



class PostGet(BaseModel):
    id: int
    text: str
    topic: str
    like_count: int

    class Config:
        orm_mode = True


class FeedGet(BaseModel):
    user_id: int
    user: UserGet
    post_id: int
    post: PostGet
    time: datetime.datetime
    action: str

    class Config:
        orm_mode = True




