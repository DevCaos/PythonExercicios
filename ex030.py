nome = str(input('Qual o seu nome? '))
casa = float(input('Qual o valor da casa? '))
sal = float(input('Qual o seu salário? '))
anos = int(input('Em quantos anos você vai pagar a casa? '))

prestacao = casa / (anos * 12)

if sal * 0.7 <= prestacao:
    print(f'Empréstimo NEGADO. A prestação de R${prestacao:.2f} excede o valor de 30% do seu salário R${sal:.2f}')
else:
    print(f'Empréstimo APROVADO. Sua parcela é de R${prestacao:.2f}')
