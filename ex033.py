nome = str(input('Qual o seu nome? '))
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

media = (nota1 + nota2) / 2
if media <= 5:
    print(f'{nome}, você está REPROVADO. Nota = {media}')
elif media <= 6.9:
    print(f'{nome}, você está na RECUPERAÇÃO. Nota = {media}')
else:
    print(f'{nome}, você está APROVADO. Nota = {media}')
