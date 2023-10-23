destino = str(input('Qual o seu destino final? ')).strip()
dtc = float(input('Qual a distância em km? '))

if dtc <= 200:
    preco = dtc * 0.50
else:
    preco = dtc * 0.45
print(f'Para ir até {destino}, a passagem custa R${preco:.2f}')
