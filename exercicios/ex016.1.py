x = float(input('\033[1;34mDigite um valor:\033[m '))
c = {"clean": '\033[m',
     "black": '\033[1;34m',
     "green": '\033[1;32m'}
print(f'{c["black"]}O valor digitado foi {x} e sua porção inteira é {c["green"]}{x:.0f}{c["clean"]}')
