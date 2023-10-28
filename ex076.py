dado = []
tudo = []
maior = menor = 0
while True:
    dado.append(str(input('Digite o seu nome: ')))
    dado.append(int(input('Qual seu peso? ')))
    if len(tudo) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    tudo.append(dado[:])
    dado.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print(f'Você cadastrou {len(tudo)} pessoas.')
print(f'O maior peso foi de {maior}kg. Peso de ', end=' ')
for p in tudo: # ele vai varrer a lista principal(tudo) em busca do p[1]
    if p[1] == maior:
        print(f'[{p[0]}] ', end=' ')
print()
print(f'O menor peso foi de {menor}kg. Peso de ', end=' ')
for p in tudo:
    if p[1] == menor:
        print(f'[{p[0]}] ', end=' ')
print()