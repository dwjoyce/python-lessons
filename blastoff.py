# blastoff.py
# Program to ask a number of seconds, and then count down to that number

import time

number_seconds = input("How many seconds? ")
number_seconds = int(number_seconds)

for num in range(number_seconds, 0, -1):
    print(num, "*" * num)
    time.sleep(1)

print("BLAST OFF!!!")
