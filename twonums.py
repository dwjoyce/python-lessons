# twonums.py
# Input two numbers, print out in order from least to greatest, with total and average

a = raw_input('Please enter the first number: ')
b = raw_input('Please enter the second number: ')

a = int(a)
b = int(b)

print "The correct order of the numbers is:",

if a <= b:
    print a,b
else:
    print b,a

total = a + b
average = float(total) / 2  # or: average = total / 2.0

print 'Sum of numbers is', total, 'and the average is', average
