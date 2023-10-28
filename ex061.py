teste = homens = mulher = 0
while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Digite a idade: '))
    if idade > 18:
        teste += 1
    sexo = str(input('Digite o sexo [M/F] ')).upper().strip()[0]
    if sexo == 'M':
        homens += 1
    elif idade < 20 and sexo == 'F':
        mulher += 1
    print('-=' * 15)
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    print('-=' * 15)
    if continuar == 'N':
        break

print(f'Você saiu do programa.')
print('~' * 30)
print(f'Existem {teste} pessoas com mais de 18 anos.')
print(f'Foram {homens} homens cadastrados.')
print(f'Foram {mulher} mulheres cadastradas com menos de 20 anos.')
print('~' * 30)
