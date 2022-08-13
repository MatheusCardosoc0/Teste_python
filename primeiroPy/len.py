text = input("Digite um texto ")
sizeText = len(text)
halfText = text[:int(sizeText / 2)]

print(text[sizeText - 2:sizeText])
print(halfText[-2:])
