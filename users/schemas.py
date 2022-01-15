from typing import Optional

from pydantic import BaseModel


class GroupBase(BaseModel):
    title: str
    description: Optional[str] = None


class GroupCreate(GroupBase):
    pass


class Group(GroupBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    groups: list[Group] = []

    class Config:
        orm_mode = True
