# wordcounter.py
# Ask the user the file to read, and then step through the file one line
# at a time, and finally output the number of lines, words and characters.

filename = raw_input('Please enter the name of the file: ')
my_file = open(filename)

num_lines = 0
num_words = 0
num_chars = 0

for line in my_file:
    num_lines = num_lines + 1
    words = line.split()
    num_words = num_words + len(words)
    num_chars = num_chars + len(line)


print 'Lines:%d, words:%d, characters:%d' % (num_lines, num_words, num_chars)

my_file.close()
