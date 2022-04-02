print('=-=-=-='*7)
print('Analisador de Triângulos')
print('=-=-=-='*7)
r1 = float(input('Primeiro seguimento: '))
r2 = float(input('Segundo seguimento: '))
r3 = float(input('Terceiro seguimento: '))
if r1 < r2 + r3 and r2 < r3 +r1 and r3 < r1 + r2:
    print('{:.2f}, {:.2f}, e {:.2f} PODEM FORMAR um triângilo!'.format(r1, r2 ,r3))
else:
    print('{:.2f}, {:.2f}, e {:.2f} NÃO PODEM FORMAR um triângulo!'.format(r1, r2 ,r3))
