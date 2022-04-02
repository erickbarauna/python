s = float(input('Qual é o salário do funcionário: R$'))
if s > 1250:
    x = 0.10 * s + s
else:
    x = 0.15 * s + s
print('Quem ganhava R${:.2f}, agora passa a ganhar R${:.2f}.'.format(s, x))
