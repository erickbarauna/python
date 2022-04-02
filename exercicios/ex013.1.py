print('\033[1;33m-=\033[m'*35)
x = float(input('\033[1;33mQual o valor do funcionário?\033[m '))
y = float(input('\033[1;33mQual o desconto adicionado?\033[m '))
c = {"clean": '\033[m',
     "yellow": '\033[1;33m',
     "blackred": '\033[1;30;41m'}
print(f'{c["yellow"]}O funcionário que ganhava {c["blackred"]}R${x}{c["clean"]}{c["yellow"]}, com {c["blackred"]}{y}%{c["clean"]}{c["yellow"]} de almento, vai passar a ganhar {c["blackred"]}R${x * y / 100 + x}{c["clean"]}')
print('\033[1;33m-=\033[m'*35)
