import math

user_input = input('Enter radius: ')
r = float(user_input)

area = math.pi * r ** 2
circumference = 2 * math.pi * r

print('Radius', r)
print('Area', area)
print('Circumference', circumference)
