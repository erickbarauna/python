from random import randint
lista = ('pedra', 'papel', 'tesoura')
pc = randint(0, 2)
print('''Suas opções:
[0] PEDRA 
[1] PAPEL
[2] TESOURA''')
x = int(input('Qual é a sua jogada? '))
print('\033[1;30m-=\033[m'*15)
print('O computador escolheu {}'.format(lista[pc]))
print('O jogador jogou {}'.format(lista[x]))
print('\033[1;30m-=\033[m'*15)
if pc == 0:
    if x == 0:
        print('EMPATE!')
    elif x == 1:
        print('JOGADOR VENCE!')
    elif x == 2:
        print('COMPUTADOR VENCE!')
elif pc == 1:
    if x == 0:
        print('COMPUTADOR VENCE!')
    elif x == 1:
        print('EMPATE!')
    elif x == 2:
        print('JOGADOR VENCE!')
elif pc == 2:
    if x == 0:
        print('JOGADOR VENCE!')
    elif x == 1:
        print('COMPUTADOR VENCE!')
    elif x == 2:
        print('EMPATE!')



