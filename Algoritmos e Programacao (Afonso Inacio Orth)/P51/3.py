#

lista_in = []
lista_out = []

c = 0

while c < 10:
  c += 1
  value = float(input("Valor {}: ".format(c)))
  if (value >= 10) and (value <= 20):
    lista_in.append(value)
  else:
    lista_out.append(value)

print(lista_in)
print(lista_out)