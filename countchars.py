# countchars.py
# Python program to count the number of characters in a sentence,
# given that A is 1, B is 2 and so on.

a_value = ord('A')

sentence = input('Please enter your sentence: ')
sentence = sentence.upper()

total = 0

for letter in sentence:
    total = total + ord(letter) - a_value + 1

print('The total of your sentence is:', total)
