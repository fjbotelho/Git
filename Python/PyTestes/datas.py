import pandas as pd
import datetime

date_1 = datetime.datetime.now()

print ('\n')
print ('-> datetime.datetime.now()')
print (date_1)
print (date_1.__repr__())
print (type(date_1))

date_2 = datetime.date.today()

print ('\n')
print ('-> datetime.date.today()')
print (date_2)
print (date_2.__repr__())
print (type(date_2))

date_3 = pd.Timestamp(1993, 6, 7, 15, 16, 0)

print ('\n')
print ('-> pd.Timestamp(1993, 6, 7, 15, 16, 0)')
print (date_3)
print (type(date_3))
print (date_3.normalize())

# Aritemetica com datas
TODAY = pd.Timestamp('today').normalize()
END = TODAY + datetime.timedelta(days=15)

print ('\n')
print ('Aritemética ...')
print ('-> pd.Timestamp(\'today\').normalize()')
print (TODAY)
print ('-> TODAY + datetime.timedelta(days=15)')
print(END)

# Criar lista de datas
calendar1 = pd.DataFrame(index=pd.date_range(start=TODAY, end=END))
print ('-> pd.DataFrame(index=pd.date_range(start=TODAY, end=END))')
print (calendar1.head())
calendar2 = pd.DataFrame(index=pd.date_range(start=TODAY, end=END, freq="B"))
print ('pd.DataFrame(index=pd.date_range(start=TODAY, end=END, freq="B"))')
print ('Só business days')
print (calendar2.head())