x = int(input('Anos de nascimento: '))
print(f'Quem nasceu em {x} tem {2021 - x} anos em 2021.')
if 2021 - x < 18:
    print(f'Ainda faltam {18 - (2021 - x)} anos para o alistamento.')
    print(f'Seu alistamento será em {2021 + (18 - (2021 - x))}. ')
elif 2021 - x > 18:
    print(f'Você já deveria ter se alistado há {(2021 - x) - 18} anos.')
    print(f'Seu ano de alistamento foi {2021 - ((2021 - x) - 18)}')
else:
    print('Você tem que se alistar IMEDIATAMENTE!')
"""PARA SABER O ANO ATUAL O CÓD É:
FROM DATETIME IMPORT DATE.
ANO ATUAL = DATE.TODAY().YEAR."""