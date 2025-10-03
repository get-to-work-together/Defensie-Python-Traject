
filename = 'Cursus/Dag 3/data.txt'
# filename = 'Cursus\\Dag 3\\data.txt'
# filename = r'Cursus\Dag 3\data.txt'
# filename = '/Users/peter/Computrain/_InCompany/Defensie/Python Traject/Cursus/Dag 3/data.txt'

with open(filename) as f:
    for line in f.readlines():
        line = line.strip()
        id, voornaam, achternaam, woonplaats = line.split(';')
        if 'ee' in woonplaats:
            print(voornaam, achternaam)