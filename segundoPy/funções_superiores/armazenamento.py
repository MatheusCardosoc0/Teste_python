
def Validation(p, min, max):
  x = int(input(p))
  while(x > max or x < min):
    x = int(input(p))
  global result
  result = x
  return x

def CriaArquivo(ArquivoNovo):
  try:
    a = open(ArquivoNovo, 'wt+')
    a.close()
  except:
    print('Erro na criação do arquivo')
  else:
    print('Arquivo {} foi criado'.format(ArquivoNovo) )

def VerifiArquivo(arquivoName):
  try:
    a = open(arquivoName, 'tr')
    a.close()
  except:
    return False
  else:
    return True

Arquivo = "games.txt"
if(VerifiArquivo(Arquivo)):
  print('Arquivo encontrado')
else:
  print('Arquivo inexistente')
  CriaArquivo(Arquivo)

def listarArquivo(arquivoNome):
  try:
    a = open(arquivoNome, 'rt')
  except:
    print('Erro ao ler o arquivo')
  else:
    print(a.read())
  finally:
    a.close()


def cadastrar(nomeArquivo, nomeJogo, nomeVideogame):
  try:
    a = open(nomeArquivo, 'at')
  except:
    print('Erro ao brir o arquivo')
  else:
    a.write('{}/{}\n'.format(nomeJogo, nomeVideogame))
  finally:
    a.close()


while True:
  print("Digite 0 para encerrar\nDigite 1 para adicionar um novo membro a lista\nDigite 2 para mostrar a lista\n")

  per = Validation('Digite uma opção ',0, 2)

  if(per == 1):
    print('Cadastrando novo item')
    nomeJogo =input('Qual o nome do jogo: ')
    nomeViedeogame =input('Qual o nome do videogame: ')
    cadastrar(Arquivo, nomeJogo, nomeViedeogame)
  elif(per == 2):
    print('Mostrando lista')
    listarArquivo(Arquivo)
  else:
    print('Encerrando...')
    break
