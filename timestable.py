# timestable.py
# Print out 12 times table using two for loops, one to do the rows, and the other
# for the columns inside each row

for row in range(1, 13):
    for col in range(1, 13):
        print(row * col, end=" ")
    print()

# To print out in a nicer format with the numbers in neat columsn, use the following print statement:
#       print("%3d " % (row * col), end="")
