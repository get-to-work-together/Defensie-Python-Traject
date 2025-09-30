name = 'Guido'
age = 62

print(name, 'is', age, 'jaar oud.')
print(name + ' is ' + str(age) + ' jaar oud.')
print('{} is {} jaar oud.'.format(name, age))
print('%s is %d jaar oud.' % (name, age))

print(f'{name} is {age} jaar oud.')

print(name)
print(name.upper())
print(name.lower())
print(name.swapcase())
print(name.replace('o', 'x'))
print(name.lower().count('g'))
print(name.lower().find('d'))
