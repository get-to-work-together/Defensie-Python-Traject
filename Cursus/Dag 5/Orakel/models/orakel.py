import random


wijsheden = [
    'Een dag niet gelachen is een dag niet geleefd.',
    'A appel a day keeps the doctor away.',
    'Beter één vogel in de hand dan tien in de lucht.',
    'Eén zwaluw maakt nog geen zomer.'
]

def geef_wijsheid():
    return random.choice(wijsheden)

# -------------------------------------------------------

if __name__ == '__main__':

    print(geef_wijsheid())
