
from sqlalchemy import Integer, String, Column, CheckConstraint
from sqlalchemy.orm import relationship 
from database import Base

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

    transactions = relationship("Transaction", back_populates="category")

    __table_args__ = (
        CheckConstraint("name != ''"),
    )

