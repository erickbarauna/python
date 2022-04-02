x = float(input('\033[1;36mQuanto dinheiro vocÊ tem na carteira? \033[1;32mR$'))
c = {'clean': '\033[m',
     'blackandblue': '\033[1;30;45m',
     'blackandgreen': '\033[1;30;42m'}
print('\033[1;36m--'*20)
print('Com {}R${}{} \033[1;36mvocê pode comprar {}U${:.2f}{}.'.format(c['blackandgreen'], x, c['clean'], c['blackandgreen'], x * 5.01, c['clean']))
print('\033[1;36m--'*20)