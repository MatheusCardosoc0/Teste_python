j = int(input("Digite o começo da tabuada: "))
p = int(input("Digite o fim da tabuada: "))

for i in range(j, p ,1):
  print('tabuada do {}'.format(i))
  for a in range(1, 11, 1):
    print("{} * {} = {}".format(i, a, i * a))