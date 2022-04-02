'''x = int(input('Digite um número para\ncalcular seu fatorial: '))
n = x
f = 1
print('Calculando {}! = '.format(x), end='')
while n > 0:
     print('{}'.format(n), end='')
     print(' x ' if n > 1 else ' = ', end='')
     f = f * n
     n -= 1
print('{}'.format(f))'''
x = int(input('\033[4mDigite um número para\ncalcular seu fatorial: '))
f = 1
print('Calculando {}! = '.format(x), end='')
for c in range(x, 0, -1):
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
print('{}'.format(f))
