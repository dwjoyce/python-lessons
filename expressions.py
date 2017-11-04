'''
An expression in programming is a value or a combination 
of values with operators

Expression -> Expression Operator Expression
Expression -> Number
Expression -> String
Expression -> Boolean
Expression -> (Expression)
Operator   -> + - * / % ** == != > < >= <= and or not
Number     -> 0 1 2 3 ...
String     -> 'a' 'b' 'c' ...
Boolean    -> True False

print(<Expression>
variable_name = <Expression>
if <Expression>:
    do something

For example:

10 + 20
10 + 20 * 2
(10 + 20) * 2
10 == 11
10 != 11 or 10 < 12
'''

# You can store values in variables using the equals '=' sign,
# similar to using a calculator, e.g.

M1 = 10
M2 = 20
M3 = M1 + M2   # so M3 will be 30

# ... but in programming, we can use more descriptive names,
# variables are usually in lowercase with the underscore '_'
# between each word, e.g.

hours_worked = 40
pay_per_hour = 5.50
pay_per_week = hours_worked * pay_per_hour
print('You are paid', pay_per_week)

# we can get values from the user using the input function

user_name = input('What is your name? ')
print('Hello', user_name)

# and convert into an integer when we need a number...

user_age_str = input('What is your age? ')
user_age = int(user_age_str)
print('You are', user_age + 10, 'years old in 10 years time!')

# Compare numbers with comparison operators...

num1 = 10
num2 = 20
if num1 == num2:
    print('num1 and num2 are the same')
elif num1 > num2:
    print('num1 is greater than num2')
else:
    print('num2 must be greater than num1')

# Let's use boolean operators to see if a car
# for sale meets our selection criteria...

car_type = input('What is the car type? ')
car_colour = input('What is the car colour? ')
car_cost = input('and what is the cost? ')
car_cost = int(car_cost)

if (car_type == 'sport' and
    (car_colour == 'red' or car_colour == 'blue') and
    car_cost < 10000):
    print('I want that car!')
else:
    print('I\'ll pass on that one!')

# without boolean operators, you would have to do the above like this...

if car_type == 'sport':
    if car_colour == 'red':
        if car_cost < 10000:
            print('I want that car!')
        else:
            print('I\'ll pass on that one!')
    elif car_colour == 'blue':
        if car_cost < 10000:
            print('I want that car!')
        else:
            print('I\'ll pass on that one!')
    else:
        print('I\'ll pass on that one!')
else:
    print('I\'ll pass on that one!')
