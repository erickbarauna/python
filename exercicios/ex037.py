x = float(input('Valor da casa: R$'))
s = float(input('Salário do camprador: R$'))
a = int(input('quantos anos de financiamento? '))
p = x / (a*12)
print('Para pagar uma casa de R${:.2f} em {} anos'.format(x, a), end='')
print(' a prestação será de R${:.2f}'.format(p))
t = s * 0.3
if p <= t:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')




