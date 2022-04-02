c = f = h = 0
while True:
    print('\033[1m---' * 20)
    print('CADASTRE UMA PESSOA')
    print('---' * 20)
    i = int(input('Idade: '))
    s = q = ' '
    if i > 18:
        c += 1
    while s not in 'MF':
        s = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if s == 'M':
            h += 1
        if s == 'F' and i < 20:
            f += 1
    while q not in 'SN':
        print('---' * 20)
        q = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if q == 'N':
        break
print(f'\033[1;32mTotal de pessoas com mais de 18 anos: {c}')
print(f'Ao todo temos {h} homens cadastrados')
print(f'E temos {f} mulheres com menos de 20 anos')
