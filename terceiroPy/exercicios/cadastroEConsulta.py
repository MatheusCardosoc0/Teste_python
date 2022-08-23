cadastro = []

def cadastrar():
  Nome = input('\nNome: ')
  Idade = input('\nIdade: ')
  profissão = input('\nProfissão: ')
  cadastros = {
    'nome' : Nome,
    'idade' : Idade,
    'profissao' : profissão,
  }
  cadastro.append(cadastros.copy())

def consultar():
  while True:
    try:
      y = int(input('\n1-para mostrar todos os dados\n2-para procurar por codigo\n3-para voltar ao menu de opções\n>>>'))
    except:
      print('erro')
      break
    if(y == 1):
      for i in cadastro:
        for a,j,p in i:
          print('{} {} {}'.format(a,j,p))



while True:
  try:
    x = int(input('\n1-para Cadastrar\n2-para consultar\n3-para sair\n>>>'))
  except:
    print('Valor invalido')
  if(x == 1):
    cadastrar()
    continue
  elif(x == 3):
    break
  elif(x == 2):
    consultar()
  else:
    print('Dado invalido')
    continue