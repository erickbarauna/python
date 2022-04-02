x = int(input('Didite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''')
y = int(input('Sua opção: '))
if y == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(x, bin(x)[2:]))
elif y == 2:
    print('{} convertido para OCTAL é igual a {}'.format(x, oct(x)[2:]))
elif y == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(x, hex(x)[2:]))
else:
    print('Opção invalida!')
