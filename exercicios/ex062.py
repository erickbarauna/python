x = int(input('Primeiro Termo: '))
r = int(input('Razão da PA: '))
t = x
c = 1
to = 0
t2 = 10
while t2 != 0:
    to = to + t2
    while c <= to:
        print('{} -> '.format(t), end='')
        t += r
        c += 1
    print('PAUSA')
    t2 = int(input('Quantos termos você quer mostrar mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(to))
