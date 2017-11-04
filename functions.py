# functions.py
# A number of functions, increasing in capability, all called below

def do_nothing():
    pass

def say_hello():
    print("Hello")

def say_hello_times(number):
    print("Hello" * number)

def say_msg_times(message, number):
    print(message * number)
    
def stars(rows, cols):
    for r in range(rows):
        print("*" * cols)
    
def isPalindrome(word):
    palindrome = True
    for position in range(len(word)):
        if word[position] != word[-1 - position]:
            palindrome = False
    return palindrome
    
def find_longest_word(sentence):
    word_list = sentence.split()
    longest_word = ""
    for word in word_list:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word
    
def two_nums(num1, num2):
    # return the largest of either num1 or num2
    if num1 > num2:
        return num1
    else:
        return num2
    
def largest_num(numbers):
    # return the largest out of the list numbers
    if len(numbers) > 0:
        largest = numbers[0]
        for num in numbers:
            if num > largest:
                largest = num
        return largest
    return None
    
def is_prime_number(number):
    # return whether the number is prime (True) or not (False)
    for num in range(2, number):
        if number % num == 0:
            return False
    return True

do_nothing()
say_hello()
say_hello_times(10)
say_msg_times("Programming is fun\t", 10)
stars(5, 10)
print(isPalindrome("nun"))
print(isPalindrome("racing car"))
print(isPalindrome("abba"))
print(isPalindrome("radar"))

print(find_longest_word("I have antidisestablishmentarianism"))
print(find_longest_word("The quick brown fox jumped over the lazy dog"))

print(two_nums(10, 20))  # should print out 20
print(largest_num([10, 20, 30, 40, 25, 35, 50, 15]))  # should print out 50
print(largest_num([ ]))
print(is_prime_number(25))  # should print out False
print(is_prime_number(29))  # should print out True
