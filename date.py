# Accept date from user in format DD/MM/YY, and print out in format: 22nd April 2014

# Rules for day postfix: 11 - 19: th, endswith 1: st, 2: nd, 3: rd, else: th

month_names = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']

date = input('What is today\'s date? ')
d, m, y = date.split('/')

if d >= '11' and d <= '19':
    postfix = 'th'
elif d.endswith('1'):
    postfix = 'st'
elif d.endswith('2'):
    postfix = 'nd'
elif d.endswith('3'):
    postfix = 'rd'
else:
    postfix = 'th'

print(d + postfix, month_names[int(m) - 1], y)
