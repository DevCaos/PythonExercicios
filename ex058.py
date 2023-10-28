n = s = quant = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
    quant += 1
print(f'Foram digitados {quant} números. A soma vale {s}')
