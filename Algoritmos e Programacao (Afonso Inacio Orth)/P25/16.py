#

valor = [1,2,3]
maior = valor[0]

for i in valor:
  if maior < i:
    maior = i

print("{} é o maior valor".format(maior))