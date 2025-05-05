from datetime import datetime

from pydantic import BaseModel, Field

class CreateProduct(BaseModel):
    name: str
    description: str
    price: int
    image_url: str
    stock: int
    category: int


class CreateCategory(BaseModel):
    name: str
    parent_id: int | None = None


class CreateUser(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: str
    password: str


class CreateReview(BaseModel):
    comment: str
    comment_date: datetime = Field(default_factory=datetime.now())
    grade: int
    is_active: bool = True