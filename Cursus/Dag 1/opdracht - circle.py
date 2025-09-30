import math

# invoer
user_input = input('Geef de diameter van een cirkel: ')
r = float(user_input) / 2

# berekeningen
area = math.pi * r * r
circumference = 2 * math.pi * r

# uitvoer
print('Straal:', r)
print('Oppervlakte:', area)
print('Omtrek:', circumference)