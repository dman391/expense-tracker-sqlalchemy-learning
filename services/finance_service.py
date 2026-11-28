from sqlalchemy.orm import Session
from models import Account
from sqlalchemy import select, update, delete, func
from models import Category
from models import Transaction

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

    def add_transaction(self, account_id, category_id, amount, date, type, description=None):
        new_transaction = Transaction(account_id, category_id, amount, date, type, description)
        self.db.add(new_transaction)
        self.db.commit()

    def get_transaction(self, transaction_id):
        transaction = select(Transaction).where(Transaction.id == transaction_id)
        print(self.db.execute(transaction).all())

    def update_transaction(self, transaction_id, *, amount=None, category_id=None, date=None, type=None, description=None):
        update_trans = update(Transaction).where(transaction.id = transaction_id).values(
           amount = amount,
           category_id = category_id,
            date = date,
           type = type,
           description = description
        )
        self.db.execute(update_trans) #only if insert update or delete to do the command in db
        self.db.commit() #make final
    
    def delete_transaction(self, transaction_id):
        del_stmt = delete(Transaction).where(Transaction.id == transaction_id)
        self.db.execute(del_stmt)
        self.db.commit()

    def list_transactions(self, account_id=None, start_date=None, end_date=None):
        all_valid_transactins  = select(Transaction.name).where(Transaction.date >= start_date, Transaction.date <= end_date)
        print(self.db.execute(all_valid_transactins).all())

    #def monthly_summary(self, year, month, account_id=None):

    def spending_by_category(self, start_date, end_date, account_id=None):
        
    #def reconcile_balances(self):