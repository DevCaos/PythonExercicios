from datetime import datetime
cadastro = {}
cadastro["nome"] = str(input('Digite seu nome: '))
nasc = int(input('Seu ano de nascimento: '))
cadastro["idade"] = datetime.now().year - nasc
cadastro["ctps"] = int(input('Carteira de trabalho (0 não tem): '))
if cadastro["ctps"] != 0:
    cadastro["contrat"] = int(input('Ano de contratação: '))
    cadastro["salario"] = float(input('Salário: '))
    cadastro["aposentadoria"] = cadastro["contrat"] - nasc + 35
for k, v in cadastro.items():
    print(f'{k} tem o valor {v}')
