x = ['macaco', 'cavalo', 'peixe']
print(x)

x.append('cabra')
print(x)

x[2] = 'urso'
print(x)

x.remove('cavalo')
print(x)

print()

y = x[:]
y.append('avestruz')
print(y)
print(x)

z = x
z.append('gorila')
print(z)
print(x)

print(x[1][0])

for i in x:
    print(i, end=' e ')
