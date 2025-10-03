

def say_hallo(name, n=1):
    for i in range(n):
        print(f'Hallo {name}')
    print('Fijne dag verder.')


def book_flight(fromairport, toairport, numadults=1, numchildren=0):
    print(f"\nFlight booked from {fromairport} to {toairport}")
    print(f"Number of adults: {numadults}")
    print(f"Number of children: {numchildren}")


def calculate_bmi(weight, height):
    bmi = weight / height ** 2
    return bmi


# ----------------------------------------------

# say_hallo('Peter')
# say_hallo('Stefan', 5)


# book_flight('AMS', 'LHR', 2, 2)
# book_flight('AMS', 'LHR', 2)
# book_flight('AMS', 'LHR')

# book_flight(numchildren=3, fromairport="LGW", toairport="NCE")


w = int(input('Geef gewicht: '))
h = float(input('Geef lengte: '))

bmi = calculate_bmi(w, h)

print(f'Jouw BMI is {bmi}')
