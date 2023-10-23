from datetime import date
nome = str(input('Qual o seu nome? '))
ano = int(input('Qual seu ano de nascimento? '))
atual = date.today().year - ano

if atual <= 9:
    print(f'{nome}, você é MIRIM.')
elif atual <= 14:
    print(f'{nome}, você é INFANTIL.')
elif atual <= 19:
    print(f'{nome}, você é JUNIOR.')
elif atual <= 25:
    print(f'{nome}, você é SÊNIOR.')
else:
    print(f'{nome}, você é MASTER')
