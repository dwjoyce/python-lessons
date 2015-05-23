# Print out month name using a number input by the user.
# Check whether number is between 1 and 12 before indexing list.

month_names = ['January','February','March','April','May','June',
               'July','August','September','October','November','December']

month_num_str = raw_input("Please enter the month number: ")
month_num = int(month_num_str)

if month_num >= 1 and month_num <= 12:
    print month_names[month_num - 1]
else:
    print 'That\'s not a valid month number!'
