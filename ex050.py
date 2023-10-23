sexo = str(input('Qual o seu sexo? [M/F] ')).strip().upper() [0] # esse [0] é pra pegar apenas a 1ª letra digitada
while sexo != 'M' and sexo != 'F':
    sexo = str(input(f'Dados inválidos. Informe novamente: ')).strip().upper() [0]
print(f'Sexo {sexo} registrado.')
