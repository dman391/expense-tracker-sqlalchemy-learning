from database import Base, engine, Sessionfactory
import models
from services.finance_service import FinanceService

Base.metadata.create_all(engine)


with Sessionfactory() as session:
    finance = FinanceService(session)

#keeping things inside the with means we dont need to worry about resource control or having to do roll backs ourself

    finance.list_accounts()

    finance.list_categories()