x = float(input('Qual seu peso? (Kg) '))
y = float(input('Qual é sua altura? (m) '))
z = x / (y ** 2)
print(f'O IMC dessa pessoa é {z:.1f}')
if z < 18.5:
    print('Você está ABAIXO DO PESO')
elif 18.5 <= z < 25:
    print('Você está em PESO IDEAL')
elif 25 <= z < 30:
    print('Você está em SOBREPESO')
elif 30 <= z < 40:
    print('O IMC está em OBESIDADE')
else:
    print('O IMC está em OBESIDADE MÓRBIDA')
