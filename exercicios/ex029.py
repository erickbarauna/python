v = int(input('Qual a velocidade do carro? '))
if v > 80:
    print('MULTADO! Excedeu o limite permitido que é de 80Km/h')
    y = (v - 80) * 7
    print('Você deve pagar uma multa de R${}'.format(y))
print('Tenha um bom dia! e dirija com segurança.')