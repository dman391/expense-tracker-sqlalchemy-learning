from database import Base
from sqlalchemy import Integer, String, Column, ForeignKey, Float, Date
from sqlalchemy import CheckConstraint





class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True)
    amount_id = Column(Integer, ForeignKey("accounts.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))
    amount = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
    type = Column(String, nullable=False, )
    description = Column(String, nullable=True)
    

    #the checks are sql syntax not python
    __table_args__ = (CheckConstraint("type = 'income' OR type = 'expense'"),
        CheckConstraint("amount > 0")
    )

