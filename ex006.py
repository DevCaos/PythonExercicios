nome = input('Digite o seu nome:')
carteira = float(input('Quantos reais você tem na carteira? R$'))
dolar = carteira / 3.27

print(f'Olá {nome}! Você tem atualmente R${carteira}. Na taxa de câmbio atual, você teria US{dolar:.1f}.')