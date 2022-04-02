p = float(input('Valor do produto: '))
d = float(input('Desconto Aplicado: '))
x = (d / 100)
y = (x * p)
w = y - p
print('O produto que custava R${}, na promoção de {}% vai custar R${}'.format(p, d, w))
