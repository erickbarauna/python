p = float(input('Preço do produto: R$'))
d = float(input('Desconto à vista: '))
s = float(input('Juros se parcelado: '))
x = (p * d / 100) - p
y = (p * s / 100) + p
print('Se comprar o produto à vista, pagará apenas R${:.2f}, agora se parcelar pagará R${:.2f}'.format(x, y))
