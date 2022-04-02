from time import sleep
print('\033[1;33m-='*36)
la = float(input('\033[1;30;42mLargura da parede:\033[m '))
al = float(input('\033[1;30;42mAltura da parede:\033[m '))
print('\033[1;33m-='*36)
c = {'Clean': '\033[m',
     'blackandgreen': '\033[1;30;42m',
     'blackandyellow': '\033[1;30;43m'}
print('{}Sua parede tem a dimensão de {}{}x{} {}e sua área é de {}{:.2f}m².{}'.format(c['blackandgreen'], c['blackandyellow'], la, al, c['blackandgreen'], c['blackandyellow'], la*al, c['Clean']))
print('\033[1;33m-='*36)
sleep(4.9)
print('{}Quantos litros de tinta você precisa para pintar essa parede??!!{}'.format(c['blackandgreen'], c['Clean']))
sleep(4.5)
print('{}Para pintar essa parede você precisara de.....{}'.format(c['blackandgreen'], c['Clean']))
sleep(3.6)
print('{}Calma ai deixa eu pensar....{}'.format(c['blackandgreen'], c['Clean']))
sleep(3.8)
x = str(input('{}Quer mesmo saber :( ?{} '.format(c['blackandgreen'], c['Clean']))).strip().lower()
print('\033[1;33m-=' * 36)
if x == 'sim' or x == 'quero':
     print('{}Só me da trabalho...{}'.format(c['blackandgreen'], c['Clean']))
     sleep(3.4)
     print(f'{c["blackandgreen"]}Eu acho que para pintar essa parede você precisará de {c["blackandyellow"]}{la * al / 2:.2f}l{c["blackandgreen"]} de tinta :).{c["Clean"]}')
elif x in 'não nao':
     print('Obrigado amigo, você é um amigo!')
print('\033[1;33m-=' * 36)
