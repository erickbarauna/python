x = float(input('Qual é a distancia da sua viagem: '))
print('Você esta preste de fazer uma viagem de {:.1f}Km'.format(x))
y = x * 0.50 if x <=200 else x * 0.45
print('E preço da sua passagem será de R${:.2f}.'.format(y))
