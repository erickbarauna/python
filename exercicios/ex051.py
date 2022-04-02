print('\033[1m====' * 10)
print('         10 TERMOS DE UMA PA')
print('====' * 10)
t = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
d = t + (10 - 1) * r
for c in range(t, d + r, r):
    print(c, end=' -> ')
print('ACABOU!')

