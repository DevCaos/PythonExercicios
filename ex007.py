altura = float(input('Digite a altura da parede em metros:'))
largura = float(input('Digite a largura da parede em metros:'))
tinta = float(input('Digite o valor do litro da tinta:'))

m2 = altura * largura
litros = m2 / 2
valor = tinta * litros
print(f'A área da parede é de: {m2}')
print(f'Vai precisar de {litros} litros de tinta.')
print(f'O valor gasto é de R$ {valor}')