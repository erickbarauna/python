times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoence', 'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')

print('-='*15)
print(f'Lista de Times {times}')
print('-='*15)

print(f'Os 5 primeiros são {times[0:5]}')
print('-='*15)
print(f'Os últimos 4 são {times[-4:]}')
print('-='*15)
print(f'Times em ordem alfabética {sorted(times)}')
print('-='*15)
print(f'O Chapecoence está na posição {times.index("Chapecoence")+1}')