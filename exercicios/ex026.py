frase = str(input('Digíte uma frase: ')).upper().strip()
print('A letra A aprece {} vezes'.format(frase.count('A')))
print('A letra A aparece a primeira vez na posição {}'.format(frase.find('A')+1))
print('A letra A aparece a ultima vez na posição {}'.format(frase.rfind('A')))
