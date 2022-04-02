s = c = x = 0
while x != 999:
    x = int(input('Digite um número [999 para parar]: '))
    if x != 999:
        s += x
        c += 1
print('Você digitou {} números e a soma entre eles foi {}.'.format(c, s))
