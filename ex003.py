nome = input('Digite o seu nome:')
idade = int (input('Digite a sua idade:'))

idade1 = idade + 1
idade0 = idade - 1
dobro = idade * 2
triplo = idade * 3
raiz = idade ** (1/2)
print(f'Olá {nome}, sua idade é {idade}. Ano passado você tinha {idade0} e ano que vem você terá {idade1}')
print(f'O dobro da sua idade é {dobro} o triplo da sua idade é {triplo} e a raiz quadrada é {raiz:.3f}')