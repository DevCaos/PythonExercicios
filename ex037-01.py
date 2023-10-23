from random import randint
from time import sleep
print('-=' * 27)
print('Será quee você ganha de mim no pedra, papel e tesoura?')
print('-=' * 27)
sleep(0.5)
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint (0, 2)
print('''
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual é a sua jogada? '))
print('-=' * 11)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-=' * 11)
if computador == 0:
    if jogador == 0:
        print('Empate!')
    elif jogador == 1:
        print('\033[1:32m Jogador vence! \033[m')
    elif jogador == 2:
        print('\033[1:31m Computador vence!\033[m')
    else:
        print('Jogada inválida!')
elif computador == 1:
    if jogador == 0:
        print('\033[1:31m Computador vence!\033[m')
    elif jogador == 1:
        print('Empate!')
    elif jogador == 2:
        print('\033[1:32m Jogador vence! \033[m')
    else:
        print('Jogada inválida!')
elif computador == 2:
    if jogador == 0:
        print('\033[1:32m Jogador vence! \033[m')
    elif jogador == 1:
        print('\033[1:31m Computador vence!\033[m')
    elif jogador == 2:
        print('Empate!')
    else:
        print('Jogada inválida!')
else:
    print(f'Jogada inválida! Sua opção {jogador} não é um número válido.')

