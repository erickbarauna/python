x = float(input('\033[1;31mIndique a temperatura em °C:\033[m '))
c = {"clean": '\033[m',
     "red": '\033[1;31m',
     "green": '\033[1;32m'}
print(f'{c["red"]}A temperatura de {c["green"]}{x}°C{c["red"]} corresponde a {c["green"]}{(x * 1.8) + 32}°F.{c["clean"]}')

