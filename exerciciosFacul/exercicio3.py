print('Bem vindo ao programa de feijoada do Matheus Cardoso Luiz Costa')

preco = 0


def volumeFeijoada():
    while True:
        try:
            volume = float(input('Qual o volume da feijoada que deseja? '))
        except:
            print('Dado invalido')
            continue
        if (volume < 300 or volume > 5000):
            print('Volume maior ou menor que o permitido')
            continue
        else:
            break
    global preco
    volumePreco = volume * 0.08
    preco += volumePreco


def opcaoFeijoada():
    print('\nQual feijoada você deseja?')
    print('b - Básica(feijão + paiol + costelinha)')
    print('p - Premium(feijão + paiol + costelinha + partes do porco)')
    print('s - Suprema(feijão + paiol + costelinha + partes do porco + charque + calabresa + bacon) \n ')

    while True:
        opcao = input('>>>> ')
        if (opcao != 'b' and opcao != 'p' and opcao != 's'):
            print('opção invalida')
            continue
        else:
            global preco
            if (opcao == 'b'):
                preco *= 1
                break
            elif (opcao == 'p'):
                preco *= 1.25
                break
            elif (opcao == 's'):
                preco *= 1.50
                break

def acompanhamentoFeijoada():
  print('\nEscolha um acompanhamento')
  print('\n0 - não desejo acompanhamento (encerrar pedido)')
  print('1 - 200g de arroz \n2 - 150g de farofa especial')
  print('3 - 100g de couve cozida \n4 - 1 laranja descascada')

  while True:
    try:
      acompanhamento = int(input('>>> '))
    except:
      print('Digite 0 caso queira encerrar o pedido')
    if(acompanhamento > 4 and acompanhamento < 0):
      print('não há esta opção')
      continue
    else:
      global preco
      if(acompanhamento == 0):
        print('Encerrandoo pedido...')
        break
      elif(acompanhamento == 1):
        preco += 5
        continue
      elif(acompanhamento == 2):
        preco += 6
        continue
      elif(acompanhamento == 3):
        preco += 7
        continue
      elif(acompanhamento == 4):
        preco += 3
        continue


volumeFeijoada()
opcaoFeijoada()
acompanhamentoFeijoada()
print('Valor a ser pago {}'.format(preco))
