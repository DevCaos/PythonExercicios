from random import randint
qnt = 0
while True:
    escolha = int(input('Escolha um número: '))
    jogo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    random = (randint(1, 10))
    soma = escolha + random
    if jogo == 'P' and soma % 2 == 0:
        print(f'Você jogou {escolha} e o PC jogou {random}. A soma é {soma} PAR')
        print(f'Você VENCEU!')
        qnt += 1
    elif jogo == 'I' and soma % 2 == 1:
        print(f'Você jogou {escolha} e o PC jogou {random}. A soma é {soma} ÍMPAR')
        print(f'Você VENCEU!')
        qnt += 1
    else:
        print('-=' * 20)
        print(f'Você escolheu {escolha} e o PC {random}. Você perdeu.')
        print(f'Você ganhou {qnt} jogos na sequência.')
        print('-=' * 20)
        break
