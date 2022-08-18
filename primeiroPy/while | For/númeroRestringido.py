def NumberCorrect(answer, x, y):
  pergunta = float(input(answer))
  while(pergunta < x or pergunta > y):
     pergunta = float(input(answer))
  return pergunta

s1 = NumberCorrect('Digite um número entre 1 e 20 ',1,20)
print('O número {} serve /n programa encerrado'.format(s1))
  