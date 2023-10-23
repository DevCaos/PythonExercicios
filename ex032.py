from datetime import date
nome = str(input('Qual o seu nome? '))
ano = int(input('Em que ano você nasceu? '))
alistar = date.today().year - ano
tempo = 18 - alistar
passou = alistar - 18


if alistar < 18:
    print(f'{nome}, ainda faltam {tempo} ano(s) para se alistar ao serviço militar.')
elif alistar == 18:
    print(f'{nome}, já está na hora de você se alistar ao serviço militar.')
else:
    print(f'{nome}, já passou {passou} anos do tempo de se alistar ao serviço militar.')