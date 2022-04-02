x = float(input('Primeira nota: '))
y = float(input('Segunda nota: '))
z = (x + y) / 2
print(f'Tirando {x} e {y}, a média do aluno é {z:.1f}')
if z < 5:
    print('O aluno está REPROVADO!')
elif 7 > z >= 5:
    print('O aluno está de RECUPERAÇÃO!')
elif z >= 7:
    print('O aluno está APROVADO!')
