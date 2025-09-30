jaar = int(input('Welk jaar is het? : '))

is_leapyear = jaar % 4 == 0

# print(jaar, is_leapyear)

if is_leapyear:
    print(f'{jaar} is een schrikkeljaar.')
else:
    print(f'{jaar} is een NIET schrikkeljaar.')

print('Klaar!!!')



age = 45

if age > 21:
    aanhef = 'meneer'
else:
    aanhef = 'jongeman'



aanhef = 'meneer' if age > 21 else 'jongeman'