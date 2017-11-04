# threenums.py
# Input three numbers, print out in order, with total and average.

# Input three numbers numbers
num1 = input("Please enter the first number: ")
num2 = input("Please enter the second number: ")
num3 = input("Please enter the third number: ")

# Convert from string to integer
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

# Print out in correct order
print("The correct order of the numbers is: ", end="")

if (num1 <= num2) and (num2 <= num3):    # if num1 <= num2 <= num3:
    print(num1, num2, num3)
elif (num1 <= num3) and (num3 <= num2):  # elif num1 <= num3 <= num2:
    print(num1, num3, num2)
elif (num2 <= num1) and (num1 <= num3):  # elif num2 <= num1 <= num3:
    print(num2, num1, num3)
elif (num2 <= num3) and (num3 <= num1):  # elif num2 <= num3 <= num1:
    print(num2, num3, num1)
elif (num3 <= num1) and (num1 <= num2):  # elif num3 <= num1 <= num2:
    print(num3, num1, num2)
else:
    print(num3, num2, num1)

# Calculate total and average
total = num1 + num2 + num3
average = total / 3

print("Sum of numbers is", total, "and the average is", average)
