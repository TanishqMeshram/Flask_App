from pydantic import BaseModel # For pydantic model we call it schema
from typing import List


# Schema for blog
class Blog(BaseModel):
    title: str
    body: str
    # class Config():
    #     orm_mode = True


class User(BaseModel):
    name: str
    email: str
    password: str


class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog]
    # class Config():
    #     orm_mode = True


class ShowBlog(BaseModel):
    # We can modify the response by specifying it . To enable it cange the Blog to BaseModel .
    title: str 
    body: str
    creator: ShowUser
    # class Config():
    #     orm_mode = True
    

class login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None