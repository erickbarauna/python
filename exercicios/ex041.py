x = int(input('Ano de nascimento: '))
y = 2021 - x
if y <= 9:
    print(f'O atleta tem {y} anos.\nClassificação: MIRIM')
elif y <= 14:
    print(f'o atleta tem {y} anos.\nClassificação: INFANTIL')
elif y <= 19:
    print(f'O atleta tem {y} anos.\nClassificação: JÚNIOR')
elif y <= 25:
    print(f'O atleta tem {y} anos;\nClassificação: SÊNIOR')
else:
    print(f'O atleta tem {y} anos.\nClassificação: MASTER')
