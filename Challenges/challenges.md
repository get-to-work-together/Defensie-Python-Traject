---
# Challenge 1 - Encode Morse

Create a function that takes a string as an argument and returns the Morse code equivalent.

#### Examples

```python
encode_morse("EDABBIT CHALLENGE") ➞ ". -.. .- -... -... .. -   -.-. .... .- .-.. .-.. . -. --. ."

encode_morse("HELP ME !") ➞ ".... . .-.. .--.   -- .   -.-.--"
```

#### This dictionary can be used for coding:

char_to_morse = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
  '6': '-....', '7': '--...', '8': '---..', '9': '----.',
  '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
  '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
}

#### Notes
* Ouput should be International Morse Code, and use the standard conventions for symbols not defined inside the ITU recommendation (see Resources).
* Input value can be lower or upper case.
* Input string can have digits.
* Input string can have some special characters (e.g. comma, colon, apostrophe, period, question mark, exclamation mark).
* One space " " is expected after each character, except the last one.


---
# Challenge 2 - Hangman

Create a function that, given a phrase and a number of letters guessed, returns a string with hyphens - for every letter of the phrase not guessed, and each letter guessed in place.

### Examples
```python
hangman("helicopter", ["o", "e", "s"]) ➞ "-e---o--e-"

hangman("tree", ["r", "t", "e"]) ➞ "tree"

hangman("Python rules", ["a", "n", "p", "r", "z"]) ➞ "P----n r----"

hangman("He's a very naughty boy!", ["e", "a", "y"]) ➞ "-e`- a -e-y -a----y --y!"
```

### Notes
* The letters are always given in lowercase, but they should be returned in the same case as in the original phrase (see example #3).
* All characters other than letters should always be returned (see example #4).


---
# Challenge 3 - Happy Number

A happy number is a number which yields a 1 by repeatedly summing up the square of its digits. If such a process results in an endless cycle which is 4, then the number is said to be an unhappy number.

Sample computation:
```
139 = 1^2 + 3^2 + 9^2 = 1 + 9 + 81 = 91
91 = 9^2 + 1^2 = 81 + 1 = 82
82 = 8^2 + 2^2 = 64 + 4 = 68
68 = 6^2 + 8^2 = 36 + 64 = 100
100 = 1^2 + 0^2 + 0^2 = 1 + 0 + 0 = 1
```
We stopped at 1 (because continuing it will be an endless cycle), thus, 139 is a happy number.

```
67 = 6^2 + 7^2 = 36 + 49 = 85
85 = 8^2 + 5^2 = 64 + 25 = 89
89 = 8^2 + 9^2 = 64 + 81 = 145
145 = 1^2 + 4^2 + 5^2 = 1 + 16 + 25 = 42
42 = 4^2 + 2^2 = 16 + 4 = 20
20 = 2^2 + 0^2 = 4 + 0 = 4 
```
We stopped at 4 (because continuing it will be an endless cycle), thus, 67 is an unhappy number.

Create a function that accepts a number and determines whether the number is a happy number or not. Return True if so, False otherwise.

Examples
```
is_happy(67) ➞ False

is_happy(89) ➞ False

is_happy(139) ➞ True

is_happy(1327) ➞ False

is_happy(2871) ➞ False

is_happy(3970) ➞ True
```

### Notes
* You are expected to solve this challenge via recursion.


---
# Fraction Class

Write a class that let's you work with fractions. You should be able to instantiate a fraction with a nominator and a denominator, e.g. **Fraction(nominator, denominator)**. Adding, subtracting, multiplying and dividing two fractions should be supported by the operators +, -, * en / respectively. A fraction should be represented as nominator/denominator when printed. Fractions should also always be symplified.

### Examples:
```
f1 = Fraction(3, 5)
f2 = Fraction(1, 3)

print(f1)          # prints 3/5 
print(f2)          # prints 1/3 

print(f1 + f2)     # prints 14/15 
print(f1 - f2)     # prints 4/15 
print(f1 * f2)     # prints 1/5
print(f1 / f2)     # prints 1 4/5 
print(3 * f1)      # prints 3/5
```