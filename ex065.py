times = ('parmeiras', 'framengo', 'curintia', 'inter', 'fruminense',
         'atletico pr', 'atletico mg', 'america mg', 'goias', 'santos',
         'bragantino', 'fortal', 'botafogo', 'sao paulo', 'ceara', 'cuiaba',
         'curitiba', 'avai', 'atletico go', 'juventude')
for colocaçao in times:
        print(f'{colocaçao}')
print(times[0:5])
print(times[-4:])
print(f'{sorted(times)}')
print(f'O Santos está na {times.index("santos")+1}ª posição')
