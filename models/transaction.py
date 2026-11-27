from database import Base
from sqlalchemy import Integer, String, Column, ForeignKey, Float, Date, CheckConstraint
from sqlalchemy.orm import relationship





class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey("accounts.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))
    amount = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
    type = Column(String, nullable=False, )
    description = Column(String, nullable=True)
    
    account = relationship("Account", back_populates="transactions")

    category = relationship("Category", back_populates="transactions")

    #the checks are sql syntax not python
    __table_args__ = (CheckConstraint("type = 'income' OR type = 'expense'"),
        CheckConstraint("amount > 0")
    )

