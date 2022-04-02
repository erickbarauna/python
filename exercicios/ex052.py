n = int(input('Digite um número: '))
cont = 0
for c in range(1, n+1):
    if n % c == 0:
        cont += +1
        print('\033[1;34m', end=' ')
    else:
        print('\033[1;31m', end=' ')
    print(c, end=' ')
print('\033[m\033[1m\nO número {} foi divisivel {} vezes'.format(n, cont))
if cont == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')


