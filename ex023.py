vel = float(input('Qual a velocidade do carro em km/h? '))
if vel > 80:
    multa = (vel - 80) * 7
    print(f'Você foi mutado em R${multa:.2f} por ultrapassar a velocidade de 80km/h.')
else:
    print(f'Não atingiu a velocidade máxima. Você está seguro!')