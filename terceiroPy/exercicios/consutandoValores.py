carros = [{'nome': 'honda', 'data': 2010, 'codigo': 2326}, {'nome': 'mercedes', 'data': 2110, 'codigo': 2326}, {
    'nome': 'mercedes', 'data': 2210, 'codigo': 2326}, {'nome': 'mercedes', 'data': 2310, 'codigo': 2326}]

x = int(input('consutar por data: '))

for i in carros:
  if(i['data'] == x):
    for a,b in i.items():
      print('{} = {}'.format(a,b))

#for x in carros:
   #for i, j in x.items():
        #print('{} = {}'.format(i, j))
