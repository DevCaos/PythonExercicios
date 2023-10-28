from random import randint
from time import sleep
from operator import itemgetter
"""valor = dict() *****MINHA FORMA FOI ESSA*****
valor['jogador1'] = randint(1, 6)
valor['jogador2'] = randint(1, 6)
valor['jogador3'] = randint(1, 6)
valor['jogador4'] = randint(1, 6)
max_val = max(valor['jogador1'], valor['jogador2'], valor['jogador3'], valor['jogador4'])
print(f'Valores sorteados:')
sleep(0.5)
print(f'O jogador1 tirou {valor["jogador1"]}')
print(f'O jogador2 tirou {valor["jogador2"]}')
print(f'O jogador3 tirou {valor["jogador3"]}')
print(f'O jogador4 tirou {valor["jogador4"]}')
print()
print(f'O maior valor foi {max_val}')"""

jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list()
print(f'Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.5)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(f'-=' * 20)
for i, v in enumerate(ranking):
    print(f'{i+1}ª lugar: {v[0]} com {v[1]}.')
    sleep(0.5)
