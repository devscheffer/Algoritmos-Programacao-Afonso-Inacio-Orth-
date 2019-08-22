#

from random import randint

def create_lista(nt, lista1):
  c = 0
  while c < nt:
    n = randint(0,50)
    lista1.append(n)
    c += 1

lista_input = []
create_lista(50,lista_input)
print(lista_input)

maior = lista_input[0]
menor = lista_input[0]
soma = 0
c = 0

for i in lista_input:
  if maior < i:
    maior = i
  if menor > i:
    menor = i
  soma += i
  c += 1
avg = soma / c

print(
  """
  Lista: {}
  Maior: {}
  Menor: {}
  Media: {}
  """.format(
    lista_input,
    maior,
    menor,
    avg
  )
)