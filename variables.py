# variables.py
# Variables allow us to use names to refer to values.  They are called "variables" because
# their value changes during the course of running the program.

# The name on the left using the '=' operator is set to the value on the right

M = 10
print(M)
print(M + 20)

M = M + 50
print(M)

# The name of the variable is up to you.
a = 10
b = 20
c = a * b + 12 / 3  # this will amount to: a * b + 4

# The print command can receive a number of items, with a comma between each
print(a, b, c)

# You can then make variable c refer to a different value
c = b + a
c = c + 1  # add one onto the value of c, and assign it back to c, same as 'c += 1'

print('New value for c is', c)

# Variables names must start with a letter, but can be followed by
# numbers or underscore '_' character

my_name = 'Fred'
my_age = 99

print('Hello there', my_name, 'you are', my_age, 'years old.')
