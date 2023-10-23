soma = 0 # acumulador
contador = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        contador = contador + 1 # ou contador += 1
        soma = soma + c # ou soma += c
print(f'A soma de todos os {contador} valores solicitados é {soma}')
