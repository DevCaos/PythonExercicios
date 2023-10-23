num1 = int(input('Escreva um número inteiro: '))
num2 = int(input('Escreva outro número inteiro: '))

if num1 > num2:
    print(f'O primeiro valor {num1} é maior.')
elif num2 > num1:
    print(f'O segundo valor {num2} é maior.')
else:
    print(f'Não existe valor maior, {num1} e {num2} são iguais. ')
