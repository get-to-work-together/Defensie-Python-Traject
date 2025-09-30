import random

filename = 'Cursus/Dag 2/basiswoorden-gekeurd.txt'

f = open(filename)

regels = f.readlines()

f.close()

# print(len(regels))
print(regels[:100])

geheim = random.choice(regels).strip()
