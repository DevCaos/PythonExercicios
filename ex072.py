# nesse exercicio, vemos a importância do sort()
lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:   # se for o primeiro valor ou último valor
        lista.append(n)
        print(f'Adicionado ao final da lista...')
    else:  # se tiver no meio
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print(f'Os valores digitados em ordem foram {lista}')
