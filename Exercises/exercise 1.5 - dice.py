import random

die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
die3 = random.randint(1, 6)
die4 = random.randint(1, 6)
die5 = random.randint(1, 6)

total = die1 + die2 + die3 + die4 + die5

print('Thrown', die1, die2, die3, die4, die5)
print('Total', total)



















# n = 5
# total = 0
# for i in range(n):
#     die = random.randint(1, 6)
#     print('Thrown', die)
#     total += die
#
# print('Total', total)





#   DRY - Don't Repeat Yourself








# die = []
# for _ in range(20):
#     die.append(random.randint(1, 6))
#
# print('Thrown', die)
# print('Total', sum(die))




# die = [random.randint(1, 6) for _ in range(5)]
#
# print('Thrown', die)
# print('Total', sum(die))





# die = []
# for _ in range(5):
#     die.append( random.randint(1, 6) )
#
# print('Thrown', die)
# print('Total', sum(die))


# die = [random.randint(1, 6) for _ in range(5)]
#
# print('Thrown', die)
# print('Total', sum(die))
