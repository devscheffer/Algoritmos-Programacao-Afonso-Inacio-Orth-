#

from random import randint


def create_lista_input(lista_input):
  n = 50
  c = 0

  while c < n:
    n2 = randint(0, 100)
    c += 1
    lista_input.append(n2)

lista_input = []
create_lista_input(lista_input)

maior = lista_input[0]
for i in lista_input:
  if maior < i:
    maior = i

print(lista_input)
print(maior)