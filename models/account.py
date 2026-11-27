
from sqlalchemy import Integer, String, Column, Float, CheckConstraint
from sqlalchemy.orm import relationship
from database import Base 

class Account(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    balance = Column(Float, nullable=False, server_default = '0.0')

    #built on the foreign key relationships and adds the ability for objects to act with each other instead of needing to do queries joining them up for example
    transactions = relationship("Transaction", back_populates="account")
    
    __table_args__ = (
        CheckConstraint("balance >= 0"),
        CheckConstraint("name != ''")
    )

