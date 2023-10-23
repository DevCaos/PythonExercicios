frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras) # desconsiderar os espaços
inverso = ''
# poderia usar invez do for... inverso = junto[::-1]
for letra in range(len(junto) -1, -1, -1): # -1 pra tirar a ultima "letra invisivel", vai até a letra -1 que é o zero, e vai voltando "invertido"
    inverso += junto[letra]
print(junto, inverso)
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
