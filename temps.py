# temps.py
# Ask user whether to convert from celsius to fahrrenheit, or vice versa
# then input temperature, and print out converted temperature

print 'Celsius to Fahrenheit converter.'

selection = raw_input('Is your temperature in celsius or fahrenheit, c/f? ')

if selection == 'c':
    ctemp = int( raw_input('What is the temperature in celsius? ') )
    ftemp = (9 / 5.0) * ctemp + 32
    print 'The temperature in fahrenheit is', ftemp
elif selection == 'f':
    ftemp = int( raw_input('What is the temperature in fahrenheit? ') )
    ctemp = (5.0 / 9) * (ftemp - 32)
    print 'The temperature in celsius is', ctemp
else:
    print 'What was that?'
