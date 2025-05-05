from sqlalchemy import Integer, Column, ForeignKey, String, DateTime, Boolean

from app.backend.db import Base

class Reviews(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False, index=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False, index=True)
    comment = Column(String, nullable=True)
    comment_date = Column(DateTime)
    grade = Column(Integer)
    is_active = Column(Boolean, default=True)
