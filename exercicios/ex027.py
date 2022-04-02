frase = str(input('Digíte seu nome: ')).strip()
s = frase.split()
print('Seu primeiro nome é {}'.format(s[0]))
print('Seu ultimo nome é {}'.format(s[len(s)-1]))
