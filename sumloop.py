# sumloops.py
# Keep asking user for a number, and when 'stop' is entered,
# print out the total and average

sum = 0
numbers = 0

while True:
    num = input("Enter number, or quit to stop: ")
    if num == "quit":
        break
    sum = sum + int(num)
    numbers = numbers + 1

print("Sum is", sum)
print("Average is", sum/numbers)
