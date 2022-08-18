print('Calculo de conta de energia')

print('digite I para Industrial')
print('digite R para residencial')
print('digite C para comercial')

typeInstalation = input('Qual o tipo de instalaçaõ? ')
kWh = float(input('Quantos kWh foram gastos? '))

if (kWh <= 500 and typeInstalation == 'R'):
    print('O valor a pagar é R${}'.format(kWh * 0.40))
elif (kWh <= 100 and typeInstalation == 'C'):
    print('O valor a pagar é R${}'.format(kWh * 0.55))
elif (kWh <= 5000 and typeInstalation == 'I'):
    print('O valor a pagar é R${}'.format(kWh * 0.55))
elif (kWh > 500 and typeInstalation == 'R'):
    print('O valor a pagar é R${}'.format(kWh * 0.65))
elif (kWh > 1000 and typeInstalation == 'C'):
    print('O valor a pagar é R${}'.format(kWh * 0.60))
elif (kWh > 5000 and typeInstalation == 'I'):
    print('O valor a pagar é R${}'.format(kWh * 0.60))
else:
    print('Dados digitados de forma errada')
