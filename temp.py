# temp.py
# Ask for temperature in fahrenheit, and print out the equivelent in celsius

fah_str = input("What is the temperature in fahrenheit? ")
fah = int(fah_str)
cel = 5 / 9 * (fah - 32)
print("The temperature in celsius is", cel)
