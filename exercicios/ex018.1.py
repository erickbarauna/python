import math
x = float(input('Digite que você deseja: '))
t = math.tan(math.radians(x))
c = math.cos(math.radians(x))
s = math.sin(math.radians(x))
co = {"clean": '\033[m',
      "green": '\033[1;32m'}
print(f'O angulo {co["green"]}{x}{co["clean"]}\nTem o cosseno de {co["green"]}{c:.2f}{co["clean"]}\nO tem seno de {co["green"]}{s:.2f}{co["clean"]}\nE a tangente de {co["green"]}{t:.2f}{co["clean"]}')
x = str(input('digite algo: '))
print(len(x))
print(3*5+4**2)
