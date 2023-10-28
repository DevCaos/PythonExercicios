total = caro = cont = 0
nomebarato = ''
while True:
    print('-' * 25)
    print('LEITOR DE PRODUTO E PREÇO')
    print('-' * 25)
    produto = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço: R$ '))
    total += preco
    cont += 1
    if cont == 1:
        barato = preco
        nomebarato = produto
    else:
        if preco < barato:
            barato = preco
            nomebarato = produto
    if preco > 1000:
        caro += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'O total gasto R$ {total:.2f}')
print(f'{caro} produtos mais de R$ 1000.00')
print(f'{nomebarato} foi o produto mais barato. Custando R$ {barato}')
