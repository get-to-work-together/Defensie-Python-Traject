import string
import random

n_lower = 3
n_upper = 3
n_digits = 1
n_special = 1
minimal_length = 12

n_extra = max([0, minimal_length - n_lower - n_upper - n_digits - n_special])

lower = random.choices(string.ascii_lowercase, k = n_lower)
upper = random.choices(string.ascii_uppercase, k = n_upper)
digits = random.choices(string.digits, k = n_digits)
special = random.choices(string.punctuation, k = n_special)
extra = random.choices(string.ascii_letters + string.digits, k = n_extra)

all = lower + upper + digits + special + extra

random.shuffle(all)

password = ''.join(all)

print(f'Your new password is: {password}')