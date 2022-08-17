
print("")
print("Bem vindo a pizzaria do Matheus Cardoso Luiz Costa")
print("")
print("                    Cardapio                        ")
print("| Código | Descrição  | pizza Média | Pizza Grande |")
print("| 21     | Napolitana |     R$20.00 |      R$26.00 |")
print("| 22     | Margherita |     R$20.00 |      R$26.00 |")
print("| 23     | Calabresa  |     R$25.00 |      R$32.00 |")
print("| 24     | Toscana    |     R$30.00 |      R$39.00 |")
print("| 25     | Portuguesa |     R$30.00 |      R$39.00 |")
print("")
# variavel preco que armazenara todos os valores dos preços já somados
preco = 0

#while primario que deixa em um luping o programa até que seja finalizado
while True:
    #while secundario para evitar problemas com conteúdo de variaveis ainda não executadas
    while True:
        #variavel que armazena o tamanho da pizza
        tamanho = input("Qual o tamanho da pizza que deseja (M/G): ")
        if (tamanho != 'M' and tamanho != 'G'):
            print('Opção invalida')
            continue
        #variavel que armazena o tipo da pizza
        pizza = int(input("Coloque o codigo do produto desejado: "))

        if (pizza > 20 and pizza < 26):
            if (pizza == 21):
                pizzaName = 'Napolitana'
                if(tamanho == 'G'):
                   preco += 26.00
                elif(tamanho == 'M'):
                   preco += 20.00
                break
            elif (pizza == 22):
                pizzaName = 'Margherita'
                if(tamanho == 'G'):
                   preco += 26.00
                elif(tamanho == 'M'):
                   preco += 20.00
                break
            elif (pizza == 23):
                pizzaName = 'Calabresa'
                if(tamanho == 'G'):
                   preco += 32.00
                elif(tamanho == 'M'):
                   preco += 25.00
                break
            elif (pizza == 24):
                pizzaName = 'Toscana'
                if(tamanho == 'G'):
                   preco += 39.00
                elif(tamanho == 'M'):
                   preco += 30.00
                break
            elif (pizza == 25):
                pizzaName = 'Portuguesa'
                if(tamanho == 'G'):
                   preco += 39.00
                elif(tamanho == 'M'):
                   preco += 30.00
                break
        else:
            print('opção invalida')
            continue
    print(
        'Você pediu uma pizza {}, deseja pedir mais alguma coisa?'.format(pizzaName))
    print('0 para Não')
    print('1 para Sim')
    repetir = input('>>>')
    #estrutura que validará a decisão se pedirá mais algum produto ou não
    if(repetir != '0' and repetir != '1'):
         print('opção invalida')
         repetir = input('>>>')
    elif(repetir == '1'):
        continue
    else:
       break
#imprime o valor final dos produto(s) comprados
print('O total a ser pago é R${}'.format(preco))
