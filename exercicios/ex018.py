from math import cos, sin, radians, tan
an = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(an))
print('O angoludo de {} tem o SENO de {:.2f}'.format(an, seno))
cosseno = cos(radians(an))
print('O angulo de {}, tem o COSSENO de {:.2f}'.format(an, cosseno))
tangente = tan(radians(an))
print('O angulo de {}, tem a TANGENTE de {:.2f}'.format(an,tangente))
