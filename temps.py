# temps.py
# First ask what the current temperature in, and depending on the answer convert
# this temperature from celsius to fahrenheit, or vice versa.

selection = input("Is your current temperature in fahrenheit, c/f? ")

if selection == "f":
    # Convert from fahrenheit to celsius
    far_str = input("What is the temperature in fahrenheit? ")
    far = int(far_str)
    cel = (5.0 / 9) * (far - 32)
    print("The temperature in celsius is", cel)
elif selection == "c":
    # Convert from celsius to fahrenheit
    cel_str = input("What is the temperature in celsius? ")
    cel = int(cel_str)
    fah = (9 / 5.0) * cel + 32
    print("The temperature in fahrenheit is", fah)
else:
    print("Enter a 'c' or 'f'!")
