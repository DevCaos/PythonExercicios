nome = input('Digite o seu nome:')
dias = int(input('Quantos dias você ficou com o carro?'))
km = int(input('Quantos Km rodados?'))

aluguel = (dias * 60) + (km * 0.15)

print(f'Olá {nome}, o senhor precisa pagar R${aluguel:.2f}')