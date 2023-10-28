from random import randint
from time import sleep
'''t = 1
print('Adivinhe o número de 0 a 10')
r1 = (random.randint(0, 10))
n1 = int(input('Seu palpite: '))
while n1 != r1:
    n1 = int(input('Você errou. \nDigite mais um número: '))
    t += 1
    if n1 == r1:
        print(f'Você acertou. O número era {r1} e você tentou {t} vezes')
'''
computador = randint(0, 10)
print('Sou seu pc... Acabei de pensar em um número entre 0 e 10.')
sleep(0.5)
print('Será que você consegue adivinhar?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente mais uma vez.')
        elif jogador > computador:
            print('Menos... tente mais uma vez.')
print(f'Acertou com {palpites} palpites!')
