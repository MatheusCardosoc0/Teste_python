print('Coloque a medida dos lados dos triangulos')

lado1 = float(input('lado 1: '))
lado2 = float(input('lado 2: '))
lado3 = float(input('lado 3: '))

if (lado1 > 0 and lado2 > 0 and lado3 > 0):
    if (lado1 + lado2 > lado3 and lado3 + lado1 > lado2 and lado2 + lado3 > lado1):
        if (lado1 == lado2 and lado2 == lado3):
            print('O triangulo é equilatero')
        elif (lado1 == lado2 or lado2 == lado3 or lado1 == lado3):
            print('O triangulo é isosseles')
        elif (lado1 != lado2 and lado2 != lado3):
            print('O triângulo é Escaleno')
    else:
        print('não é um triângulo')
else:
    print('não é um triângulo')
