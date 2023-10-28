from datetime import date
dado = {}
dado['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dado['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
dado['idade'] = date.today().year - nasc
if dado['ctps'] != 0:
    dado['contratação'] = int(input('Ano de contratação: '))
    dado['salario'] = float(input('Salário: R$ '))
    dado['aposentadoria'] = (35 - (date.today().year - dado['contratação'])) + dado['idade']
print(f'-=' * 30)
for k, v in dado.items():
    print(f'{k} tem o valor {v}')