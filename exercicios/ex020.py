from random import shuffle
n1 = str(input('Dígite um nome: '))
n2 = str(input('Dígite um nome: '))
n3 = str(input('Dígite um nome: '))
n4 = str(input('Dígite um nome: '))
n5 = str(input('Dígite um nome: '))
lista = [n1, n2, n3, n4, n5]
shuffle(lista)
print('A ordem sorteada da lista sera: ')
print(lista)