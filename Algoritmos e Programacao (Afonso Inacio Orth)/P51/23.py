  #

from random import randint


def create_lista_input(t, lista_input):
  c = 0
  while c < t:
    n = randint(1,5)
    a1 = randint(0, 5)
    r = randint(0, 5)
    c += 1
    lista_input.append([n,a1,r])

def pa(a1,r,n,lista1):
  ni = 0
  while ni < n:
    lista1.append(a1)
    a1 += r
    ni +=1

lista_input = []
create_lista_input(1,lista_input)

lista_pa = []
pa(lista_input[0][1], lista_input[0][2], lista_input[0][0],lista_pa)

total = 0
for i in lista_pa:
  total += i
print(
  """
  Valor a1: {}
  Razao da progressao: {}
  Numero de termos: {}
  """.format(
    lista_input[0][1],
    lista_input[0][2],
    lista_input[0][0]
    ))
print("Lista de termos: {}".format(lista_pa))
print("Soma dos termos: {}".format(total))
