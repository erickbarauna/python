x = input('Type something: ')
c = {'blackandpurple': '\033[1;30;45m',
     'clean': '\033[m',
     'blueandblack': '\033[1;34;40m',
     'blackandgray': '\033[7;37;40m'}
print('the primitive type of this value is {}{}{}'.format(c['blackandpurple'], type(x), c['clean']))
print('there are only spaces? ', x.isspace())
print('Is a number? {}{}{}'.format(c['blackandgray'], x.isnumeric(), c['clean']))
print('Is alphabetic? {}{}{}'.format(c['blackandblue'], x.isalpha(), c['clean']))
