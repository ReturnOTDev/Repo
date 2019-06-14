from datetime import datetime
from datetime import date

today = datetime.today()

cleanDate = datetime(2018, 12, 23, 6, 30, 0)

print((today-cleanDate).seconds)



