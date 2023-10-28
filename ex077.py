#desafio 85
num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[1].sort()
num[2].sort()
print(f'Os pares foram: {num[0]}')
print(f'Os ímpares foram: {num[1]}')
