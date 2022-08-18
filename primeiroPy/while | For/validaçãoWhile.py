while True:
  nome = input('Digite seu nome ')
  if(nome != 'Matheus'):
    continue
  senha = int(input('Digite sua senha: '))
  if(senha == 12345):
    break
print("acesso concedido")