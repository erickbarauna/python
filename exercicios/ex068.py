from random import randint
print('\033[1m=-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*20)
v = 0
while True:
    n = int(input('Digite um valor: '))
    c = randint(0, 10)
    t = n + c
    l = ' '
    while l not in 'PI':
        l = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print('=-'*20)
    print(f'Você jogou {n} e o computador {c}. Total de {n + c}')
    print('DEU PAR!' if t % 2 == 0 else 'DEU ÍMPAR!')
    print('=-' * 20)
    if l == 'P':
        if t % 2 == 0:
            print('Voce VENCEU!\nVamos jogar novamente...')
            print('=-' * 20)
            v += 1
        else:
            print('Você PERDEU!')
            print('=-' * 20)
            break
    elif l == 'I':
        if t % 2 == 1:
            print('Voce VENCEU!\nVamos jogar novamente...')
            print('=-' * 20)
            v += 1
        else:
            print('Você PERDEU!')
            print('=-' * 20)
            break
print(f'GAME OVER! Você venceu {v} vezes.')
