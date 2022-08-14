print('Digita 1 para Maçã, 2 para laranja, 3 banana')
print('Maçã = R$2.30')
print('Laranja = R$3.60')
print('Banana = R$1.85')
fruta = int(input('Qual fruta você escolhe? '))
Quantidade = int(input('Quantos? '))
if (fruta == 1):
    preco = 2.30
elif (fruta == 2):
    preco = 3.60
elif (fruta == 3):
    preco = 1.85
if (fruta == 1 or fruta == 2 or fruta == 3):
    finalValue = preco * Quantidade
    print("Você deve pagar R$%.2f" % (finalValue))
else:
  print('valor inexistente')