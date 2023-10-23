# Modelo do guanabara
nome = str(input('Digite aqui o seu nome: ')).strip()
nome2 = (nome.split()[0])

print(f""""
Letras maiúsculas: {nome.upper()}
Letras minúsculas: {nome.lower()}
Seu nome tem ao todo: {(len(nome) - nome.count(' '))} letras.
Seu primeiro nome é: {nome2.capitalize()} e ele tem {(nome.find(' '))} letras
""")

# separa = nome.split()
#print(f'Seu primeiro nome é {(separa[0], len(separa[0]))}')






