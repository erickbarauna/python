x = 'S'
c = s = ma = me = 0
while x in 'Ss':
    y = int(input('Digite um número: '))
    x = str(input('Quer continuar? [S/N] ')).strip()
    c += 1
    s += y
    mv = y
    if c == 1:
        ma = me = y
    else:
        if y > ma:
            ma = y
        if y < me:
            me = y
m = s / c
print('Você digitou {} números e a média foi {:.2f}\n'
      'O maior valor foi {} e o menor foi {}'.format(c, m, ma, me))
