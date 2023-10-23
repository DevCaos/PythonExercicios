# Tentei, não consegui fazer com que contasse sem os espaços no nome
nome = str(input('Digite o seu nome completo: ')).strip()
nome2 = (nome.split()[0])
maiuscula = nome.upper()
minuscula = nome.lower()
splitar = nome.split()
frase = len(splitar)
frase = ''.join(splitar)
frase = frase.count('')

print(f"""
O seu nome com todas as letras Maiúsculas é: {maiuscula}
O seu nome com todas as letras Minúsculas é: {minuscula}
O seu nome tem {frase} letras (sem espaços)
Seu primeiro nome é: {nome2}
""")
