sal = float(input('Qual o seu salário? '))

if sal > 1250:
    aumento = sal + (sal * 0.1)
else:
    aumento = sal + (sal * 0.15)
print(f'Parabéns! Seu salário agora é \033[1:32mR${aumento:.2f}')
