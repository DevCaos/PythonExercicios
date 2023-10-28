listagem = ('Macbook', 8999, 'Iphone 14', 12499,
            'Apple Watch', 3899, 'Ipad', 6299, 'Case p/ Macbook',
            198, 'Case p/ Iphone', 145)
print('=' * 42)
print(f'{"LISTAGEM DE PREÇOS":^42}')
print('=' * 42)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>9.2f}')
