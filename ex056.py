num = cont = soma = 0 #gambiarra
num = int(input('Digite um número [Disque 999 para parar]: '))
while num != 999:
    num = int(input('Digite um número [Disque 999 para parar]: '))
    soma += num
    cont += 1
print(f'Você digitou {cont} números e a soma entre eles foi {soma}')
