from random import randint
sorteados = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)

print(f'Os valores sorteados foram: ', end='')

maior = menor = 0
for c in range(0, 5):
    print(f'{sorteados[c]}', end=' ')
    if c == 1:
        maior = menor = sorteados[c]
    else:
        if sorteados[c] > maior:
            maior = sorteados[c]
        if sorteados[c] < menor:
            menor = sorteados[c]
print()
print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')
print(max(sorteados))
print(min(sorteados))