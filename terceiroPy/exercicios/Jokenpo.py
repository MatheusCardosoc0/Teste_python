from random import randint


valores = []


while True:
    if (valores.count(8) == 2):
        print('Você perdeu')
        break
    elif (valores.count(3) == 2):
        print('Você venceu')
        break
    else:
        try:
            print('\nEscolha\n1-pedra\n2-papel\n3-tesoura\n')
            jogador = int(input('Escolha: '))
            enemy = randint(1, 3)
            print('O enemigo escolheu {}'.format(enemy))
        except:
            print('dado digitado invalido')
            continue
        if (jogador > 3 or jogador < 1):
            print('Opção invalida')
            continue
        elif ((enemy == 1 and jogador == 3) or (enemy == 2 and jogador == 1) or (enemy == 3 and jogador == 2)):
            print('o inimigo venceu')
            valores.append(8)
            continue
        elif ((enemy == 3 and jogador == 1) or (enemy == 1 and jogador == 2) or (enemy == 2 and jogador == 3)):
            print('o jogador venceu')
            valores.append(3)
            continue
        elif (jogador == enemy):
            print('Empatou')
            continue
