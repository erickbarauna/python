from time import sleep
print('\033[1m=-=-'*10)
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
x = 0
while x != 5:
    print('\033[1;31m[ 1 ] somar\n'
          '\033[1;33m[ 2 ] multiplicar\n'
          '\033[1;34m[ 3 ] maior\n'
          '\033[1;35m[ 4 ] novos números\n'
          '\033[1;36m[ 5 ] sair do programa\033[m')
    x = int(input('\033[1m>>>>> Qual é a sua opção? '))
    if x == 1:
        print('A soma entre {} + {} é {}'.format(n1, n2, n1 + n2))
        sleep(2)
    elif x == 2:
        print('O resultado de {} x {} é {}'.format(n1, n2, n1 * n2))
        sleep(2)
    elif x == 3:
        if n1 > n2:
            print('Entre {} e {} o maior valor é {}'.format(n1, n2, n1))
            sleep(2)
        elif n2 > n1:
            print('Entre {} e {} o maior valor é {}'.format(n1, n2, n2))
            sleep(2)
    elif x == 4:
        print('Informe o número novamente.')
        sleep(2)
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    print('=-=-'*10)
print('\033[1;32mFinalizando...')
sleep(2)
print('Fim do programa! Volte sempre!')
