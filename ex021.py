n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()

print(f"""
Seu primeiro nome é: {nome[0]}
Seu último nome é: {nome[len(nome)-1]} # 0,1,2,3 -1,-2 (o -1 seria o último item da lista)
""")