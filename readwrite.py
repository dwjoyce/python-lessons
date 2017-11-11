# readwrite.py
# Read in file, and then write it out again, this time with line numbers

# Firstly read in the file "myfile.txt" into a list

my_file = open("myfile.txt")

text_lines = []

for line in my_file:
    text_lines.append(line)

my_file.close()

my_file = open("myfile-new.txt", "w")

# Now write out what we have read with a number prefixed to each line...

line_num = 1

for line in text_lines:
    my_file.write(str(line_num) + " " + line)
    line_num = line_num + 1

my_file.close()
