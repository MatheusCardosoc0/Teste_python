price = float(input("Digite um número "))
discount = float(input("Digite o desconto do produto "))

FinalValue = price - ((discount / 100) * price)

print("O valor final do produto é R$%.2f" %FinalValue)