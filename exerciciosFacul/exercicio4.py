print('Bem vindo ao controle de estoque da mercearia do Matheus Cardoso Luiz Costa')
produtos = []
sequencia = 0

def cadastrar():
  while True:
    try:
      global sequencia
      nome = input('O nome do produto: ')
      fabricante = input('O nome do fabricante: ')
      valor = float(input('O valor do produto: '))
      codigo = sequencia
      produto = {
        'nome' : nome,
        'fabricante' : fabricante,
        'valor' : valor,
        'codigo' : codigo
      }
      produtos.append(produto.copy())
      sequencia += 1
      break
    except:
      print('Ouve um erro, tente novamente')
      continue


def consultarProduto():
  while True:
    try:
      global produtos
      per = int(input('\n1-Consultar todos os produtos\n2-Consultar produto por codigo\n3-Consultar produto(s) por fabricante\n4-retornar\n>>>'))
    except:
      print('ocorreu um erro, tente novamente')
      continue
    if(per > 4 or per < 1):
      print('Opção invalida')
      continue
    elif(per == 1):
      for dados in produtos:
        for key,value in dados.items():
          print('{} = {}'.format(key,value))
    elif(per == 2):
      codigoProduto = int(input('Digite o codigo do produto: '))
      for dados in produtos:
        if(dados['codigo'] == codigoProduto):
          for key, value in dados.items():
            print('{} = {}'.format(key,value))
    elif(per == 3):
      fabricanteProduto = input('Digite o nome do fabricante do produto: ')
      for dados in produtos:
        if(dados['fabricante'] == fabricanteProduto):
          for key, value in dados.items():
            print('{} = {}'.format(key,value))
    elif(per == 4):
      print('Retornando...')
      break


def removerProduto():
  try:
    remover = int(input('Digite o codigo do produto que deseja remover: '))
    for dados in produtos:
      if(dados['codigo'] == remover):
        produtos.remove(dados)
    print('Produto removido')
  except:
    print('Codigo inexistente')




while True:
  try:
    x = int(input('\n1-Cadastrar produto\n2-Consultar produto(s)\n3-Remover produto\n4-sair\n>>>'))
  except:
    print('Ocorreu um erro, tente novamente')
    continue
  if(x > 4 or x < 1):
    print('opção invalida')
    continue
  elif(x == 1):
    cadastrar()
  elif(x == 2):
    consultarProduto()
  elif(x == 3):
    removerProduto()
  elif(x == 4):
    print('encerrando programa')
    print(produtos)
    break