print('=' * 20)
print(f"{'BANCO LIMA MEI' : ^20}")
print('=' * 20)
#print(f'LIMITE MÁXIMO DE SAQUE POR CPF R$ 5000.00')
valor = int(input('Que valor você quer sacar? R$ '))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd} ')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
