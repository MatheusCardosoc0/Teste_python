print('\nBem vindo ao programa de feijoada do Matheus Cardoso Luiz Costa\n')

#Variaveis globais
preco = 0
v = 0
acomp = 0
opc = 0


#função que pergunta e captura os dados do pedido do cliente para a variavel v
def volumeFeijoada():
    while True:
      #Sistema de validção
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
    global v
    volumePreco = volume * 0.08
    v = volumePreco
    preco += volumePreco

#função que pergunta e captura os dados do pedido do cliente para a variavel opc
def opcaoFeijoada():
    print('\nQual feijoada você deseja?')
    print('b - Básica(feijão + paiol + costelinha)')
    print('p - Premium(feijão + paiol + costelinha + partes do porco)')
    print('s - Suprema(feijão + paiol + costelinha + partes do porco + charque + calabresa + bacon) \n ')

    while True:
      #Sistema de validção
        opcao = input('>>>> ')
        if (opcao != 'b' and opcao != 'p' and opcao != 's'):
            print('opção invalida')
            continue
        else:
            global preco
            global opc
            if (opcao == 'b'):
                preco *= 1
                opc = v * 1 - v
                break
            elif (opcao == 'p'):
                preco *= 1.25
                opc = v * 1.25 - v
                break
            elif (opcao == 's'):
                preco *= 1.50
                opc = v * 1.50 - v
                break

#função que pergunta e captura os dados do pedido do cliente para a variavel acomp
def acompanhamentoFeijoada():
  print('\nEscolha um acompanhamento')
  print('\n0 - não desejo acompanhamento (encerrar pedido)')
  print('1 - 200g de arroz \n2 - 150g de farofa especial')
  print('3 - 100g de couve cozida \n4 - 1 laranja descascada')

  while True:
    #Sistema de validção
    try:
      acompanhamento = int(input('>>> '))
    except:
      print('Digite 0 caso queira encerrar o pedido')
      continue
    if(acompanhamento > 4 or acompanhamento < 0):
      print('não há esta opção')
      continue
    else:
      global preco
      global acomp
      if(acompanhamento == 0):
        print('Encerrandoo pedido...')
        break
      elif(acompanhamento == 1):
        preco += 5
        acomp += 5
        continue
      elif(acompanhamento == 2):
        preco += 6
        acomp += 6
        continue
      elif(acompanhamento == 3):
        preco += 7
        acomp += 7
        continue
      elif(acompanhamento == 4):
        preco += 3
        acomp += 3
        continue

#Chamada das funções pela ordem de perguntas sobre o pedido a serem feitas
volumeFeijoada()
opcaoFeijoada()
acompanhamentoFeijoada()
#Todos os dados capturados são imprimidos de forma separada e com os calculos já feitos
print('Valor a ser pago R${} (volume = {} + opção = {} + acompanhamento = {})'.format(preco, v, opc, acomp))
