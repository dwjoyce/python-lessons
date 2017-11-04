# twonums.py
# Input two numbers, print(out in order from smallest to largest, along with total and average

first_num_str = input("Please enter the first number: ")
second_num_str = input("Please enter the second number: ")

first_num = int(first_num_str)
second_num = int(second_num_str)

print("The correct order of the numbers is: ", end="")

if first_num < second_num:
    print(first_num, second_num)
else:
    print(second_num, first_num)

total = first_num + second_num
average = total / 2

print("Sum of numbers is", total, "and the average is", average)
