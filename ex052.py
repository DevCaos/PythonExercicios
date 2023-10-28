from time import sleep
num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
sleep(0.5)
print('-='*10)
print('       Menu')
print('-='*10)
print('''
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa''')
menu = int(input('Qual a sua opção? '))
while menu != 5:
    if menu == 1:
        soma = num1 + num2
        print(f'Valor da soma entre {num1} + {num2} é {soma}')
    #menu = int(input('Outra opção: '))
    if menu == 2:
        mult = num1 * num2
        print(f'Valor da multiplicação é {mult}')
    if menu == 3:
        if num1 == num2:
            print(f'{num1} e {num2} são iguais!')
        elif num1 > num2:
            print(f'{num1} é maior.')
        else:
            print(f'{num2} é maior.')
    if menu == 4:
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
    if menu > 5:
        print('Opção inválida. Tente novamente')
        sleep(0.5)
    sleep(1)
    print('-=' * 10)
    print('       Menu')
    print('-=' * 10)
    print('''
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa
    ''')
    menu = int(input('Outra opção: '))
print('Você saiu do programa.')







