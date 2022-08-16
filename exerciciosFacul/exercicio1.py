print('Bem vindo a loja do Matheus Cardoso Luiz Costa')

produto = float(input('Valor do produto: ')) 
quantidade = int(input('Quantidade do produto: ')) 
valorFinal = produto * quantidade 

#valor final com no maximo 2 casas decimais para melhor compreensão
print('O valor sem desconto foi: R$%.2f' % (valorFinal)) 

#só funcionará se o valor da quantidade for entre 5 e 19
if (quantidade >= 5 and quantidade <= 19): 
  #calculo do valor final menos a quantidade de desconto
    comDesconto = valorFinal - (valorFinal * (3 / 100)) 
  #valor do desconto
    desconto = 3 
elif (quantidade >= 20 and quantidade <= 99): 
    comDesconto = valorFinal - (valorFinal * (6 / 100))
    desconto = 6
elif (quantidade >= 100): 
    comDesconto = valorFinal - (valorFinal * (10 / 100))
    desconto = 10
#só funcionará se o valor da quantidade for menor que 4
else: 
    comDesconto = valorFinal - 0
    desconto = 0
#só funcionará se o valor for positivo
if (quantidade > 0):
  #texto mostrando valor final com desconto e a quantidade de desconto
    print('O valor com desconto foi: R${}  (desconto {}%)' .format(comDesconto, desconto))