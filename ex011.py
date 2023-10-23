print('Vamos calcular a hipotenusa?')
co = float(input('Digite o comprimento do cateto oposto:'))
ca = float(input('Digite o comprimento do cateto adjacente:'))

hip = (co ** 2 + ca ** 2) ** (1/2)

print(f'O comprimento da hipotenusa é {hip:.2f}')

# math.hypot(co, ca)
