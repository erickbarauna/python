from datetime import date
ano = int(input('Qual é o ano que você quer analisar? Digpite 0 para analisar esse ano:'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 == 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO!'.format(ano))
else:
    print('O ano {} NÂO È BISSEXTO!'.format(ano))