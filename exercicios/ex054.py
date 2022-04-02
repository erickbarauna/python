from datetime import date
atual = date.today().year
c = 0
d = 0
for c in range(1, 8):
    nasc = int(input('Em que ano a {}° pessoa nasceu? '.format(c)))
    idade = atual - nasc
    if idade >= 21:
        d += 1
    else:
        c += 1
print('Ao todo tivemos {} pessoas maiore de idade!'.format(d))
print('E também tivemos {} pessoas menores de idade!'.format(c))
