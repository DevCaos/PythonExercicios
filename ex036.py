from time import sleep
nome = str(input('Qual é o seu nome? '))
produto = str(input('Qual o produto? '))
valor = float(input('Qual o valor do produto: R$'))
sleep(1)
print('-='*20)
print('Gerando métodos de pagamentos...')
print('-='*20)
avista = valor - (valor * 0.1)
avistac = valor - (valor * 0.05)
parcelado = valor + (valor * 0.2)
sleep(1)
print(f'À vista dinheiro ou cheque: R${avista:.2f}')
print(f'À vista no cartão: R${avistac:.2f}')
print(f'Em até 2x no cartão: R${valor:.2f}')
print(f'Em 3x ou mais no cartão: R${parcelado:.2f}')
