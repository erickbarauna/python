n = float(input('Quanto dinheiro você tem na carteira? R$'))
d = n / 5.23
e = n / 6.37
print('Com R${} voçê pode comprar US${:.2f} ou {:.2f} euros'.format(n, d, e))
