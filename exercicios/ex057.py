s = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while s not in 'MmFm':
    s = str(input('Dados inválidos. Por favor, informe seu sexo: ')).upper()
print('Sexo {} registrado com sucesso'.format(s))
