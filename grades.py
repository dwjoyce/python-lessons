# grades.py
# Ask for a score or mark (out of a 100), and print out grade from 'A' to 'F'

score = int( raw_input('What if your score, 0-100: ') )

# Trail print with a comma, and it will append the next print onto this one
print 'Your grade is',

if score < 0 or score > 100:
    print 'invalid!'
elif score >= 90:
    print 'A'
elif score >= 80:
    print 'B'
elif score >= 70:
    print 'C'
elif score >= 60:
    print 'D'
elif score >= 50:
    print 'E'
else:
    print 'F'
