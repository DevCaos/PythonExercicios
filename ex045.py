from time import sleep
print('-='*10)
print('10 TERMOS DE UMA PA')
print('-='*10)
sleep(0.5)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = termo + (10 - 1) * razao
for c in range(termo, decimo + razao,razao):
    print (c, end='-> ')
print('FIM')
