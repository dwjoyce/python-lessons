# revision.py
# Practice the concepts in Python we have learnt so-far

# This is a comment

# Print out some strings
print "Hello, World!"
print 'Another string' + 'with a second string added on'
print 'A string with "double quotes"'
print 'A string with a quote like it\'s see?'
print '''This is a
multi-line
string'''
print '#' * 80, '\n Welcome to Python\n', '#' * 80

# We can do arithmetic too
print 10 + 5 - 3
print 10 / 5 * 3
print 99 % 5 ** 2
print 5.0 // 2  # integer divide

# We call functions to do things for us
print abs(-123)
print len('Hello there')  # length of any sequence
print ord('a')  # print out ordinal number of a character
print bin(183)  # binary of 183 decimal
print hex(183)  # hex of 183 decimal
print int('101011', 2)  # prints decimal version of binary 1010 (43)
print round(18.27521, 2)  # prints out rounded version to 2 decimal places

# It is easy to put names (variables) to save values for us
a = 10
b = a + 15
b = b + 1  # or b += 1 as a short-cut
b *= 2  # times b by 2, same as b = b * 2
s = 'Happy' + ' ' + 'Birthday'

# We can get input from the user
name = raw_input('What is your name? ')
print 'Hello there', name

# We can convert from one type to another
hours = raw_input('How many hours do you work per week? ')
wage = raw_input('What is your wage per hour in pounds sterling? ')
print 'Wow, you are paid', int(hours) * int(wage), 'pounds per week!'  # don't forget those commas!

# Using other code is easy
import turtle
p = turtle.Pen()
p.forward(100)

# Getting help in Python IDLE is easy:
# help(str)  - get help on the "str" type
# dir(__builtins__)  - list all the builtin functions
# help('modules')  - list all the supplied modules
# dir(turtle)  - list what is available inside "turtle" module, after import

# Use the if statement to take decisions
name = raw_input('What is your name? ')
if name == 'Dr Joyce':
    print 'Yes SIR!!!'
elif name == 'Fred':
    print 'Hello Fred'
elif (name == 'Bert' or  # use () to go over one line, or the continuation character: \
      name == 'Ernie'):
     print 'How\'s it going in Sesame Street?'
else:
    print 'Who on earth are you?'
    
a = 10
b = 20

if a > b:
    print 'The largest between a and b is', a
else:
    print 'The largest between a and b is', b

# Here is a short-cut, although it is a bit cryptic
print 'The largest between a and b is', a if a > b else b  # all in one line!

# Use the while loop to do repetitive tasks
a = 10
b = 20
while a < b:
    print a
    a += 1

# This loop goes on forever, until the user enters 'quit'
while True:
    name = raw_input('What\'s your name (or \'quit\' to end)? ')
    if name == 'quit':
        break
    print 'Hello', name

# To keep similar things together, use sequences like tuples or lists

# This is a tuple - it cannot be changed
months = ( 'January', 'February', 'March', 'April', 'May', 'June',
           'July', 'August', 'September', 'October', 'November', 'December' )

# This is a list, it can be changed
names = [ 'fred', 'tom', 'dick', 'harry' ]

# Changing a list
names[3] = 'bob'  # change 'harry' to 'bob'
names.append('arthur')  # appends an item called 'arthur' to the end of the list
del names[1]  # removes the second item
names = names + ['john','zippy']  # adds onto the end of the list
print names

# You can use tuples to set and swap variables around
a,b,c = 10,20,30
a,b,c = c,a,b  # a will now be 30, b will be 10, c will be 20

# and you can use tuples also for printing formatted strings
print 'Here is the sum using 10 columns: %10d' % (1234 * 1234)
print 'pi to two decimal places %.2f' % (3.141592653589793)

# You can create a list from a string
print list('The cat sat on the mat')  # this will be ['T','h','e',' ','c','a','t',' ','s','a','t',' ','o','n',' ','t','h','e',' ','m','a','t']
l = 'The cat sat on the mat'.split(' ')  # this will be ['The','cat','sat','on','the','mat']
l.reverse()  # change the order of the list, so it will be ['mat','the','on','sat','cat','The']

# and then put it back in a string
print ' '.join(l)

# Retrieving items from a sequence
print 'The first month is', months[0]  # sequences start from zero!
print 'The last name in my list is', names[-1]  # -1 is the last item in the sequence, -2 the second from last

# You can even do slices of sequences
print 'The middle four months are', months[4:8]  # this will print May, June, July, August
print 'Every other month is', months[::2]  # start:end:step, so from start to end missing every other item

# remember, indexing off the end of a list will cause an error (e.g. months[20]),
# but using out-of-range numbers in a slice is OK:
print 'Winter months are', ', '.join(months[9:20])

# We can ask Python to generate a list of numbers for us
print 'Lots of odd numbers', range(1,100,2)
print 'Lots of even numbers', range(0,100,2)

# For loops are easy ways to step through sequences
for i in range(10,20):  # print out numbers from 10 to 20
    print i

breakfast = ['bacon','egg','tomato','mushroom','bread']
for item in breakfast:
    print 'Yum, I\'m having', item, 'for breakfast.'
    
# This is how we define our own functions, one value coming in (year), one going out (boolean)
def isLeapYear(year):
    return (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0))

# and then we can use it, like so...
print 'Is 1999 a leap year:', isLeapYear(1999)
print 'Is 2000 a leap year:', isLeapYear(2000)
print 'Is 1900 a leap year:', isLeapYear(1900)
print 'Is 2004 a leap year:', isLeapYear(2004)

def lowest_highest(numbers):  # accepts a list of numbers
    lowest = min(numbers)
    highest = max(numbers)
    return lowest, highest  # returns two values

numbers = [5,10,35,15,50,20]
low,high = lowest_highest(numbers)
print 'The lowest number was', low, 'and the highest was', high

# You can form lists like this:
squares = []
for i in range(1,13):
    squares.append(i*i)
print 'Squared numbers from 1 to 12 using for loop is', squares

# Or list comprehensions provide a short-cut, and still quite readable:
squares = [ i*i for i in range(1,13) ]
print 'Squared numbers from 1 to 12 using list comprehension is', squares

# you can even include a test inside the list, so instead of this:
leap_years_1900_to_2100 = []
for year in range(1900,2101):
    if isLeapYear(year):
        leap_years_1900_to_2100.append(year)
print 'Leap years from 1900 to 2100 using a for loop loop is', leap_years_1900_to_2100

# you can do the same with a list comprehension like so:
leap_years_1900_to_2100 = [ year for year in range(1900,2101) if isLeapYear(year) ]
print 'Leap years from 1900 to 2100 using list comprehension is', leap_years_1900_to_2100

# Storing data in a file:
output_text_file = open('test.txt', 'w')
output_text_file.write('first line\n')  # need to put newline character at the end of each line
lines = ['second line\n', 'third line\n']
output_text_file.writelines(lines)
output_text_file.close()

# Read in same file, use 'for' loop
input_text_file = open('test.txt')  # 'r' read mode is default
for line in input_text_file:
    print line,  # line includes newline character
input_text_file.close()
