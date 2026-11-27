from database import Base, engine, Sessionfactory
import models
from services.finance_service import FinanceService

Base.metadata.create_all(engine)


with Sessionfactory() as session:
    finance = FinanceService(session)


#finance.create_account('joe', 50)
#finance.create_account('bob')

finance.list_accounts()
