nome = str(input('Digite o seu nome: '))
peso = float(input('Qual o seu peso? (Kg) '))
altura = float(input('Qual a sua altura? (m) '))

imc = peso / (altura ** 2)

if imc <= 18.5:
    print(f'Olá {nome}! Seu IMC é de {imc:.2f}, e você está abaixo do peso.')
elif imc <= 25:
    print(f'Olá {nome}! Seu IMC é de {imc:.2f}, e você está no peso ideal.')
elif imc <= 30:
    print(f'Olá {nome}! Seu IMC é de {imc:.2f}, e você está no sobrepeso.')
elif imc <= 40:
    print(f'Olá {nome}! Seu IMC é de {imc:.2f}, e você está OBESO.')
else:
    print(f'Olá {nome}! Seu IMC é de {imc:.2f}, e você está com obesidade mórbida.')
