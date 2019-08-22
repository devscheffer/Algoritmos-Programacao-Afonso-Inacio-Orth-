#

from random import randint

def create_lista(nt, lista1):
  c = 0
  while c < nt:
    n = randint(13,77)
    lista1.append(n)
    c += 1

lista_input = []
create_lista(3,lista_input)
print(lista_input)

lista_weight = []
for i in lista_input:
  if i % 2 == 0:
    w = 2
  else:
    w = 1
  r = i*w
  lista_weight.append([i,w,r])
print(lista_weight)
w_soma = 0
soma = 0
for j in lista_weight:
  soma += j[2]
  w_soma += j[1]
mp = (soma / w_soma)

print(
  """
  Lista: {}
  Lista com peso: {}
  Media ponderada: {}
  """.format(
    lista_input,
    lista_weight,
    mp
  )
)
