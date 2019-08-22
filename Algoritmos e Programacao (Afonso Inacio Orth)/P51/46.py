#

from random import randint


def create_client(nt, lista1):
  c = 0
  while c < nt:
    c += 1
    valor_compra = randint(100, 500)
    lista1.append([c, valor_compra])


lista_client = []
create_client(3, lista_client)
print(lista_client)

for i in lista_client:
  if i[1] >= 200:
    bonus = i[1] * 0.15
    print("Cliente: {} Bonus: {}".format(i[0], bonus))
