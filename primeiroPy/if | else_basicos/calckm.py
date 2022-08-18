day = int(input('Há quantos dias você alugou o carro? '))
km = int(input('Quantos kilometros você percorreu com o carro? '))

FinalValue = day * 60 + km * 0.15

print('O valor a ser pago é R$%.2f'%FinalValue)