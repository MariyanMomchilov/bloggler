from pydantic import BaseModel
from enum import Enum
from typing import Optional, List


class BlogType(Enum):
    LIFESTYLE = 0
    GYM = 1
    PROGRAMMING = 2


class BlogVisibility(Enum):
    PUBLIC = 0
    PRIVATE = 1


class User(BaseModel):
    email: str


class Blog(BaseModel):
    id: Optional[int]
    content: str
    type: BlogType
    author: Optional[User] = None
    visibility: Optional[BlogVisibility] = None
    # BaseModel expected to be Blog
    parents: Optional[List[BaseModel]] = None
    # BaseModel expected to be Blog
    children: Optional[List[BaseModel]] = None
