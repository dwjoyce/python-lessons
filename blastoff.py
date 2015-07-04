# blastoff.py
# Countdown timer asks the user where to start
# and prints stars beside each number

import time

start = int(input("Countdown timer:  How many seconds? "))
for i in range(start, 0, -1):
    print(i, '*' * i)
    time.sleep(1)  # number of seconds

print("BLAST OFF!")
