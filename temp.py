# temp.py
# Ask user for temperate in Fahrenheit, and print out temperate in celsius.

tf_str = raw_input('What is the temperature in fahrenheit? ')
tf = int(tf_str)

tc = (5.0 / 9) * (tf - 32)

print 'The temperature in celsius is', tc
