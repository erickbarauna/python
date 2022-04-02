from random import randint
print('\033[1mOlá Mundo! Sou um Computador...')
c = randint(0, 10)
print('Acabei de pensar em um número entre 0 e 10.')
print('Sera que você consegue adivinhar qual foi?')
p = int(input('Qual será seu palpite? '))
n = 1
while p != c:
    if p > c:
        print('Menos...Tente mais uma vez!')
    elif p < c:
        print('Mais...Tente mais uma vez!')
    p = int(input('Qual será seu palpite? '))
    n += 1
print('Acertou com {} tentativas.\033[1;32m Parabéns!'.format(n))
