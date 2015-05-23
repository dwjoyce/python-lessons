# functions.py
# A variety of functions - to use these, place this module in the same directory
# as your program, type "import functions" in your program, and call each function
# by name, e.g. functions.stars(10,20)

import string

def say_hello():
    """Prints out Hello, World!"""
    print 'Hello, World!'
    
def say_hello_times(n):
    """Prints out Hello, World! n number of times."""
    print 'Hello, World!\n' * n
    
def say_str_times(s,n):
    """Prints out specific string n number of times."""
    print (s + '\n') * n
    
def two_nums(i,j):
    """Returns the largest of two supplied numbers."""
    if i > j:
        return i
    else:
        return j
        
def day_postfix(day):
    """Turns day into string, and adds on either st, nd, rd or th postfix."""
    if day in (1,21,31):
        return "%sst" % (day)
    elif day in (2,22):
        return "%snd" % (day)
    elif day in (3,23):
        return "%srd" % (day)
    else:
        return "%sth" % (day)

def isLeapYear(year):
    """Returns True if year is a leap year, otherwise False.
    Rule: year is either divisible by 400, or it is divisible by 4 but not divisible by 100."""
    return year % 400 == 0 or (year % 4 == 0 and not year % 100 == 0)

def stars(rows, cols):
    """Display a grid of stars, the size is specified by rows, cols."""
    for i in range(rows):
        print '*' * cols

def histogram(numbers):
    """Displays a star-based histrogram."""
    for n in numbers:
        print '*' * n

def histogramVert(numbers):
    """Displays a star-based histrogram, vertically."""
    topNum = max(numbers)
    for l in range(topNum,0,-1):
        for n in numbers:
            if n >= l:
                print '*',
            else:
                print ' ',
        print
        
def find_longest_word(words):
    """Returns the longest word from a string."""
    longest = ''
    wordList = words.split(' ')
    for word in wordList:
        if len(word) > len(longest):
            longest = word            
    return longest
    
def isPalindrome(word):
    """Return True if word is a palindrome, otherwise False.  Ignores all non-alphabet letters."""
    # First create a new word with all non a..z letters removed
    newWord = ''
    for letter in word:
        if letter in string.lowercase:
            newWord = newWord + letter
    # Compare each letter from the start with the same index from the end
    for index in range(len(newWord)):
        if newWord[index] != newWord[-1 - index]:
            return False  # mismatch
    return True  # matched from start to end
    
def isPrime(num):
    """Returns True if the supplied number is a prime number, False otherwise."""
    prime = True
    if num < 2:
        prime = False  # never prime
    elif num == 2:
        prime = True   # only even number that is prime
    elif num % 2 == 0:
        prime = False  # all even numbers are not prime
    else:
        for i in range(3, num/2+1, 2):
            # if it is divisible by a number within it (up to half way), it is not prime
            if num % i == 0:
                prime = False
                break
    return prime
    
def sortList(numList):
    """sortList(iterable) --> new sorted list\n\nUse bubble sort to order list in ascending order."""
    listLength = len(numList)
    for i in range(listLength):
        number_swapped = False
        for j in range(listLength-1):
            if numList[j] > numList[j+1]:
                numList[j],numList[j+1] = numList[j+1],numList[j]
                number_swapped = True
        if not number_swapped:  # all done!
            break
    
def fib(maxNum):
    """Return a list with fibonacci sequence up to specified maximum."""
    a,b = 0,1
    numbers = [a]  # start list with just a in it
    while b < maxNum:
        numbers.append(b)
        a,b = b,a+b
    return numbers

def main():
    print 'This is the main module.'
    pass

if __name__ == '__main__':
    main()
