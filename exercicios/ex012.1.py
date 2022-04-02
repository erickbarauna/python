p = float(input('\033[1;30;47mQual é o preço do produto? R$\033[m'))
d = float(input('\033[1;30;47mQual é o desconto aplicado? %\033[m'))
c = {"clean": '\033[m',
     "blackgray": '\033[1;30;47m',
     "blackblue": '\033[1;30;46m'}
print(f'{c["blackgray"]}O produto que custava {c["blackblue"]}R${p}{c["blackgray"]}, na promoção de {c["blackblue"]}{d}{c["blackgray"]} vai custar {c["blackblue"]}R${(d/100*p-p)*-1:.2f}.{c["clean"]}')

