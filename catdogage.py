# catdogage.py
# Program to ask whether the pet is a dog or cat, and then ask for the age of the animal.
# It then prints out the equivalent human age years.
# The rules for this conversion are as follows:
#   Dogs: 11 years per year for 2 years then 4 per extra year
#   Cats: 15 years for first year, 10 for second then 4 per extra year

pet = input("Is your pet a dog or a cat? ")

if pet == "dog":
    age_str = input("What is the age of your dog? ")
    age = int(age_str)
    print("The age of your dog in human years is ", end="")
    if age == 1 or age == 2:
        print(age * 11)
    else:
        print(22 + (age - 2) * 4)
elif pet == "cat":
    age_str = input("What is the age of your cat? ")
    age = int(age_str)
    print("The age of your cat in human years is ", end="")
    if age == 1:
        print(15)
    elif age == 2:
        print(25)
    else:
        print(25 + (age - 2) * 4)
else:
    print("Sorry, I can't convert the age for that kind of animal!")
