a = int(input('Digite um número: '))
b = int(input('Digite outro: '))
c = int(input('Digite outro: '))
print('-=-=-' * 4)
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O menor é {}'.format(menor))
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior é {}'.format(maior))
print('-=-=-' * 4)
