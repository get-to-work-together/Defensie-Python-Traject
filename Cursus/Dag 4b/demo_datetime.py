import datetime
import dateutil

today = datetime.date.today()

d0 = datetime.date(2020, 1, 1)

print(today)
print(d0)

delta = today - d0

print(delta)

delta = dateutil.relativedelta.relativedelta(today, d0)

print(delta.years)


import time
t0 = time.time()

input('Het return ....')

t1 = time.time()

delta = t1 - t0

print(f'It to you {delta} seconds to hot return.')
