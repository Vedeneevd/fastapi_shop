from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.backend.db_depends import get_db

from typing import Annotated

from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Product
from app.models.review import Reviews

router = APIRouter(prefix='/review', tags=['review'])

@router.get('/')
async def all_reviews(db: Annotated[AsyncSession, Depends(get_db)]):
    reviews = await db.scalars(select(Reviews))
    return reviews.all()

@router.get('/{product_slug}')
async def products_reviews(db: Annotated[AsyncSession, Depends(get_db)], product_slug:str):
    product = await db.scalar(select(Product).where(Product.slug == product_slug))

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")  # Обработка ошибки, если продукт не найден

    # Получаем отзывы о продукте
    result = await db.execute(select(Reviews).where(Reviews.product_id == product.id))
    reviews = result.scalars().all()  # Получаем все отзывы

    return reviews

