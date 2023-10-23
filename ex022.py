import random
print('Adivinhe o número de 0 a 5: ')
r1 = (random.randint(0, 5)) # faz o computador sortear
n1 = input('Seu palpite: ')
if n1 == r1:
    print(f'Você acertou! O número era {r1}')
else:
    print(f'Você errou! O número era {r1}')
