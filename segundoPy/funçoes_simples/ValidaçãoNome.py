def NameValidation(s):
  if(len(s) < 20 and len(s) > 4):
    return 'Correto'
  else:
    return 'Errado'

print(NameValidation('uru'))
