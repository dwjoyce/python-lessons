# wordcount.py
# Ask for filename, and then count lines, words and characters, and print out the result

filename = input("Enter filename to count from: ")
my_file = open(filename)

num_lines = num_words = num_chars = 0

for line in my_file:
    num_lines = num_lines + 1
    words = line.split()
    num_words += len(words)
    num_chars += len(line)
    
my_file.close()

print("Number lines:", num_lines, "number words:", num_words, "number characters:", num_chars)
