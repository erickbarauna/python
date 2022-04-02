print('''$+LOJA+$''')
x = float(input('Preço da compra: R$'))
print('''FORMA DE PAGAMENTO 
[ 1 ] à vista no dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
y = int(input('Qual é a opção? '))
if y == 1:
    print(f'Sua compra de R${x:.2f} vai custar R${((x * 0.1) - x) * -1} no final')
elif y == 2:
    print(f'Sua compra de R${x:.2f} vai custar R${((x * 0.05) - x) * -1} no final')
elif y == 3:
    print(f'Sua compra de R${x:.2f} vai custar R${x / 2} por parcela')
else:
    d = int(input('Quantas parcelas? '))
    g = (x * 0.2) + x
    print(f'Sua compra será de {d}x de R${g / d:.2f} COM JUROS!')
    print(f'Sua compra de R${x:.2f} vai custar R${g} no final!')
