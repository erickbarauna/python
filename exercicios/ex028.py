from random import randint
from time import sleep
c = randint(0, 5) #faz o computador "pensar" em um número
print('=-=-'*13)
print('Pensei em um número entre 0 e 5, tente adivinhar!')
print('=-=-'*13)
j = int(input('Tente adivinhar o número : '))
print('=-=-'*13)
print('PROCESSANDO...')
sleep(2.5)
print('=-=-'*13)
print('O número pensado foi {}, e o seu foi {}!'.format(c, j))
if j == c:
    print('PARABÉNS! Você acertou!!')
else:
    print('QUE AZAR, Tente de novo!!')
print('=-=-'*13)
