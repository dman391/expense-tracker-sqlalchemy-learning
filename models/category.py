
from sqlalchemy import Integer, String, Column, CheckConstraint
from sqlalchemy.orm import relationship 
from database import Base

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

    accounts = relationship("Account", back_populates = 'Category')

    __table_args__ = (
        CheckConstraint("name != ''"),
    )

