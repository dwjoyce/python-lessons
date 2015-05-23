# timestable.py
# print out 12 times table

for row in range(1,13):
    for number in range(1,13):
        print "%3d" % (row * number),  # comma at end keeps output on same line
    print
