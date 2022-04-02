cont = 0
contf = 0
maisv = 0
nome = ''
for c in range(1, 5):
    print('\033[1;36m----- {}° PESSOA -----'.format(c))
    n = str(input('Nome: '))
    i = int(input('Idade: '))
    cont += i
    s = str(input('Sexo [M/F]: '))
    if s == 'F':
        if i < 20:
            contf += 1
    if s == 'M':
        maisv = i
        nome = n
print('A média de idade do grupo é {} anos'.format(cont / 4))
print('O homem mais velho tem {} anos e se chama {}'.format(maisv, nome))
print('Ao todo são {} com menos de 20 anos'.format(contf))
