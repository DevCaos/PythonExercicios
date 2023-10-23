from random import choice
escolha, pc = str(input('Escolha entre pedra, papel ou tesoura: ')).strip(), ('papel','pedra','tesoura')
random = choice(pc)
print(f'EU joguei \033[7:30:107m {escolha} \033[m x PC jogou \033[7:30:107m {random} \033[m ')

if escolha == random:
    print('-=' * 10)
    print(f'Deu empate!')
    print('-=' * 10)
elif random == 'papel' and escolha == 'pedra' or random == 'tesoura' and escolha == 'papel':
    print('-=' * 10)
    print(f' \033[1:31m Você perdeu!\033[m')
    print('-=' * 10)
elif random == 'pedra' and escolha == 'tesoura':
    print('-=' * 10)
    print('\033[1:31m Você perdeu!\033[m')
    print('-=' * 10)
else:
    print('-=' * 10)
    print(' \033[1:32m Você ganhou! \033[m ')
    print('-=' * 10)

# \033[1:31m Computador vence!\033[m
# \033[1:32m Jogador vence! \033[m
