n = float(input('Enter a value: '))
n1 = float(input('Enter another value: '))
c = {'blueandwhite': '\033[32;46m',
     'clean': '\033[m',
     'blackandpurple': '\033[1;30;45m'}
print('the sum of {} + {}, is {}{}{}'.format(n, n1, c['blackandpurple'], n1 + n, c['clean']))