l = float(input('Largura da parede: '))
al = float(input('Altura da parede: '))
ar = l * al
t = ar / 2
print('Sua perede tem a dimensão de {} x {} e sua àrea é de {:.2f}m², e com uma àrea de {:.2f}m² você precisara de {} litros de tinta.'.format(l, al, ar, ar, t))
