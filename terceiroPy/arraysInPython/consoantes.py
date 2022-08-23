nomes = ['marta', 'papel', 'chiclete', 'roteador']

for nome in nomes:
    print('\n {}, consoantes: '.format(nome.upper()), end='')
    for consoantes in nome:
        if consoantes.lower() in 'bcdfghjklmnpqrstvwxyz':
            print(consoantes.upper(), end=' ')
