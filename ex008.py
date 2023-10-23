produto = input('Nome do produto:')
valor = float(input('Qual o valor do produto? R$ '))

desconto = valor*5/100
valorf = valor - desconto

print(f'O valor do {produto} com 5% de desconto é R$ {valorf:.2f}')