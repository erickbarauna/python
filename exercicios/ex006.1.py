x = int(input('Enter a value: '))
c = {'clean': '\033[m',
     'blackandgray': '\033[1;30;47m',
     'blackandpurple': '\033[1;30;45m'}
print('Double of {}{}{}, worth {}{}{}'.format(c['blackandgray'], x, c['clean'], c['blackandpurple'], x * 2, c['clean']))
print('Triple of {}{}{}, worth {}{}{}'.format(c['blackandgray'], x, c['clean'], c['blackandpurple'], x * 3, c['clean']))
print('Square root of {}{}{}, worth {}{:.0f}{}'.format(c['blackandgray'], x, c['clean'], c['blackandpurple'], x ** (1/2), c['clean']))

