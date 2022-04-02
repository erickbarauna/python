n = i = ' '
b = c = v = me = 0
while True:
    n = str(input('Nome do Produto: ')).strip()
    p = int(input('Preço: R$'))
    x = ' '
    v += 1
    b += p
    if p >= 1000:
        c += 1
    if v == 1:
        me = p
        i = n
    else:
        if p < me:
            me = p
            i = n
    while x not in 'SN':
        x = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if x == 'N':
        break
print('Fim do Programa')
print(f'O total da compra foi R${b}')
print(f'Temos {c} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {i} que custa R${me:.2f}')
