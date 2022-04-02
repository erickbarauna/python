n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
     'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
     'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
     'dezenove', 'vinte')
while True:
    x = int(input('\033[1mDigite um número de 0 a 20: '))
    y = ' '
    if 0 <= x <= 20:
        print(f'Você digitou o número \033[1;32m{n[x].upper()}\033[m')
    while y not in 'SN':
        y = str(input('\033[1mQuer continuar? [S/N] ')).strip().upper()[0]
    if y == 'N':
        break
print('Volte sempre!')
