from sqlalchemy.orm import Session
from models import Account



class FinanceService:
    def __init__(self, db : Session) -> None:
        self.db = db

    def create_account(self, input_name, input_balance = 0):
        new_account = Account(name = input_name, balance = input_balance)
        self.db.add(new_account)
        self.db.commit()