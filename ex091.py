def maior(*num):
    cont = maior = 0
    print('-=' * 24)
    print('Analisando...')
    for valor in num:
        print(f'{valor} ', end='')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores.')
    print(f'O maior valor foi {maior}.')


maior(3, 8, 9, 4, 3, 1)
maior(4, 5, 8)
maior(1, 0, 6, 5)
maior(9)
