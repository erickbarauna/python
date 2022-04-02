print('\033[1;30m-=\033[m'*35)
x = int(input('\033[1;34mQuantos dias alugado?\033[m '))
y = float(input('\033[1;34mQuantos Km rodados?\033[m '))
print('\033[1;30m-=\033[m'*35)
c = {"clean": '\033[m',
     "blackblue": '\033[1;30;44m',
     "blue": '\033[1;34m'}
print(f'{c["blue"]}Sabendo que será cobrado R$60 por dia alugado e R$0.15 por Km percorrido.\nO total a pagar será R${c["blackblue"]}{(x * 60) + (y * 0.15)}{c["clean"]}')
print('\033[1;30m-=\033[m'*35)
