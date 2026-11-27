from sqlalchemy.orm import Session
from models import Account
from sqlalchemy import select
from models import Category

class FinanceService:
    def __init__(self, db : Session) -> None:
        self.db = db

    def create_account(self, input_name : str, input_balance = 0) -> None:
        new_account = Account(name = input_name, balance = input_balance)
        self.db.add(new_account)
        self.db.commit()

    def list_accounts(self) -> None:
        all_accounts = select(Account.name, Account.balance)
        print(self.db.execute(all_accounts).all())

    def create_category(self, input_name):
        new_category = Category(name = input_name)
        self.db.add(new_category)
        self.db.commit()

    def list_categories(self) -> None:
            all_categories  = select(Category.name)
            print(self.db.execute(all_categories).all())