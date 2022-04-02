x = int(input('Enter a value: '))
c = {'clean': '\033[m',
     'blackandgreen': '\033[1;30;42m',
     'blackandred': '\033[1;30;41m'}
print('Its predecessor {}{}{}, and successor {}{}{}'.format(c['blackandred'], x - 1, c['clean'], c['blackandgreen'], x + 1, c['clean']))