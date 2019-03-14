import datetime
now = datetime.datetime.now()
# print("Agora: ", now)
# today = now.date()
# print("Hoje: ", today)
# moment = now.time()
# print("Agora 2: ", moment)
string_date = now.strftime('%Y%m%d%H%M%S')
print("Agora 3: ", string_date)