import random

# Create out secret number, and set to a random number betweeen 1 and 100
secret_number = random.randint(1, 100)

# Create our loop variable and set to zero, and also the user's number
number_tries = 0

while number_tries < 6:  # give them 6 tries maximum
    # Get the guess from the user via the keyboard
    guess = raw_input('What is your guess (between 1 and 100)? ')
    guess = int(guess)
    
    # If the guess is correct, break out of loop,
    # otherwise tell user if the number is too low or too high
    if guess == secret_number:
        break
    elif guess < secret_number:
        print 'Too low!'
    else:
        print 'Too high!'

    # Increment the loop variable so we will hit the maximum number tries
    number_tries = number_tries + 1

# Print out result    
if guess == secret_number:
    print 'You got it right!'
else:
    print 'Wrong! The number was:', secret_number
