x = float(input('\033[1;30;45mA distance in metres: '))
c = {'clean': '\033[m',
     'blackandgreen': '\033[1;30;42m',
     'redandgray': '\033[7;31;47m'}
print('\033[1;31;47mMeasure of {}m corresponds to:\033[m \n{}{}cm.{}\033[1;31;47m\033[m\n{}{}mm.{}'.format(x, c['blackandgreen'], x * 100, c['clean'], c['blackandgreen'], x * 1000, c['clean']))
print('{}{}km.{}'.format(c['blackandgreen'], x / 1000, c['clean']))
print('{}{}hn.{}'.format(c['blackandgreen'], x / 100, c['clean']))
print('{}{}dam.{}'.format(c['blackandgreen'], x / 10, c['clean']))
