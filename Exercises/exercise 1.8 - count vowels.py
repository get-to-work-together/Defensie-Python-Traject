# invoer
s = input('Geef tekst: ').lower()

# berekeningen
number_of_a = s.count('a')
number_of_e = s.count('e')
number_of_i = s.count('i')
number_of_o = s.count('o')
number_of_u = s.count('u')
number_of_y = s.count('y')

number_of_vowels = number_of_a + number_of_e + number_of_i + number_of_o + number_of_u + number_of_y

# uitvoer
print(f"Total number of characters: {len(s)}")

print(f"Found the vowel 'a' {number_of_a} times")
print(f"Found the vowel 'e' {number_of_e} times")
print(f"Found the vowel 'i' {number_of_i} times")
print(f"Found the vowel 'o' {number_of_o} times")
print(f"Found the vowel 'u' {number_of_u} times")
print(f"Found the vowel 'y' {number_of_y} times")

print(f"Total number of vowels: {number_of_vowels}")












# print(f'De tekst bevat {len(s)} karakters')
# print(f'De tekst bevat {len(s.replace(" ", ""))} karakters (zonder spaties)')

# totaal_aantal_klinkers = 0

# for klinker in 'aeiouy':
#     n = s.count(klinker)
#     totaal_aantal_klinkers += n
#     print(f'De "{klinker}" komt {n} keer voor')

# print(f'De tekst bevat dus {totaal_aantal_klinkers} klinkers')













# s = input('Give some text: ').lower()
#
# total_number_of_vowels = 0
# for vowel in 'aeiouy':
#     n = s.count(vowel)
#     total_number_of_vowels += n
#     print(f'The vowel "{vowel}" was found {n} times.')
#
# print(f'The complete text contains {len(s)} characters.')
#
# print(f'The text contains {total_number_of_vowels} vowels.')











# s = input('Give some text: ').lower()
#
# number_of_vowels = 0
# for vowel in 'aeiouy':
#     n = s.count(vowel)
#     number_of_vowels += n
#     print(f"Vowel '{vowel}' occurs {n} times.")
#
# print(f"Total length: {len(s)}")
# print(f"Total number of vowels: {number_of_vowels}")
