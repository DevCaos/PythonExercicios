numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez')
while True:
    num = int(input('Digite um número entre 0 e 10: '))
    if 0 <= num <= 10:
        print(f'Você digitou o número: {numeros[num]}')
        outro = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if outro == 'N':
            break
print('Você saiu do programa.')
