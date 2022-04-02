from math import hypot
co = float(input('\033[1;30;47mCateto oposto:\033[m '))
ca = float(input('\033[1;30;47mCateto adjacente:\033[m '))
hi = hypot(co, ca)
c = {"clean": '\033[m',
     "blackgray": '\033[1;30;47m',
     "blackgreen": '\033[1;30;42m'}
print(f'{c["blackgray"]}A hipotenusa de vai medir {c["blackgreen"]}{hi:.2f}{c["clean"]}')
