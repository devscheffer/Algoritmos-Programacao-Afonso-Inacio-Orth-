#


c = 0
cw = 0

while cw < 5:
  cw += 1
  a = int(input("Valor: "))
  if a < 0:
    c += 1

print("Qtd de numeros negativos: {}".format(c))
