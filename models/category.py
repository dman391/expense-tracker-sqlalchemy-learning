
from sqlalchemy import Integer, String, Column
from sqlalchemy import CheckConstraint
from database import Base

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

    __table_args__ = (
        CheckConstraint("name != ''"),
    )

