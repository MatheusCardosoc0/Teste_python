def division():
  try:
    n1 = float(input("Digite um número: "))
    n2 = float(input("Digite outro número: "))
    res = n1 / n2
  except ZeroDivisionError:
    print('Divisão por zero é impossivel')
  except:
    print('Ouve algum erro')
  else:
    return print(res) 
  finally:
    print('Ieeaahh')

division()
