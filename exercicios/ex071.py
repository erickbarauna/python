x = int(input('Que valor você quer sacar? R$'))
t = x
c = 50
tc = 0
while True:
    if t >= c:
        t -= c
        tc += 1
    else:
        if tc > 0:
            print(f'Total de {tc} cédulas de R${c}')
        if c == 50:
            c = 20
        elif c == 20:
            c = 10
        elif c == 10:
            c = 1
        tc = 0
        if t == 0:
            break
print('Volte sempre ao Banco!')
