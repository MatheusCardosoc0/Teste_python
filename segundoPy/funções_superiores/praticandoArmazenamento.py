def VerifiArquivo(ArquivoNome):
    try:
        a = open(ArquivoNome, 'tr')
        a.close()
    except:
        return False
    else:
        return True


def CriarArquivo(ArquivoNome):
    try:
        a = open(ArquivoNome, 'wt+')
        a.close()
    except:
        print('Erro ao construir arquivo')
    else:
        print('Arquivo {} criado'.format(ArquivoNome))


def AcrescentArquivo(ArquivoNome, lugarNome, paisNome):
    try:
        a = open(ArquivoNome, 'at')
    except:
        print('Arquivo não encontrado')
    else:
        a.write('{} ; {}\n'.format(lugarNome, paisNome))
    finally:
        a.close()


def MostrarLista(ArquivoNome):
    try:
        a = open(ArquivoNome, 'rt')
    except:
        print('Arquivo não encontrado')
    else:
        print(a.read())
    finally:
        a.close()


arquivo = 'lugares.txt'
if (VerifiArquivo(arquivo)):
    print('arquivo encontrado')
else:
    CriarArquivo(arquivo)

while True:
    print('\n1 para acrescentar novo item\n2 para mostrar lista\n0 para sair\n')
    try:
        perm = int(input('Digite sua opção '))
    except:
        print('ocorreu um erro\n')
        continue
    if (perm > 2 or perm < 0):
        print('ocorreu um erro\n')
        continue
    if (perm == 1):
        print('Acrescentando novo item')
        lugar = input('Coloque o nome do lugar ')
        pais = input('O pais onde esse local fica ')
        AcrescentArquivo(arquivo, lugar, pais)
    elif (perm == 2):
        print('Mostrando Lista')
        MostrarLista(arquivo)
    else:
      print('Encerrando programa')
      break
