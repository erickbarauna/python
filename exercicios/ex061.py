print('Gerador de PA')
x = int(input('Primeiro termo: '))
y = int(input('Razão da PA: '))
t = x
c = 1
while c <= 10:
    print('{} -> '.format(t), end='')
    t += y
    c += 1
print('ACABOU!')

