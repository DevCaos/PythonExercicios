"""dado = dict() ****MINHA FORMA FOI ESSA****
dado['nome'] = str(input('Seu nome: '))
dado['nota'] = int(input('Sua nota: '))

print(f'Nome é igual a {dado["nome"]}.')
print(f'Média é igual a {dado["nota"]}.')
if dado['nota'] >= 7:
    print(f'Aluno aprovado')
else:
    print(f'Aluno reprovado')"""
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Nota: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'
print()
for k, v in aluno.items():
    print(f'{k} é igual a {v}')