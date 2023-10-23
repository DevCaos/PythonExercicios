from time import sleep
nome = str(input('Qual é o seu nome? '))
produto = str(input('Qual o produto? '))
valor = float(input('Qual o valor do produto: R$'))
sleep(1)
print('-='*20)
print('Gerando métodos de pagamentos...')
print('-='*20)
sleep(1)
print('''Formas de pagamento
[1] à vista dinheiro (10% de desconto)
[2] à vista cartão (5% de desconto)
[3] 2x no cartão
[4] 3x ou mais no cartão (20% de juros)
''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total = valor - (valor * 10 / 100)
elif opcao == 2:
    total = valor - (valor * 5 / 100)
elif opcao == 3:
    total = valor
    parcela = total / 2
    print(f'Olá {nome}. Sua compra ({produto}) será parcelada em 2x R${parcela:.2f}')
elif opcao == 4:
    total = valor + (valor * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print(f'Sua compra será parcelada em {totparc}x de R${parcela:.2f} com juros')
print(f'Olá {nome}. Sua compra ({produto}) de R${valor} vai custar R${total:.2f}')
