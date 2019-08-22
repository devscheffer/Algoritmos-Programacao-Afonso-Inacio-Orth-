#

from random import randint

def create_lista_input(nt, lista1):
  c = 0
  while c < nt:
    c += 1
    n = randint(0, 30)
    lista1.append(n)

def count_even_odd(lista_input):
  for i in lista_input:
    if i % 2 == 0:
      lista_even.append(i)
    else:
      lista_odd.append(i)

lista_input = []
lista_even = []
lista_odd = []
create_lista_input(10,lista_input)
count_even_odd(lista_input)

def avg(lista1):
  soma = 0
  c = 0
  for i in lista1:
    soma += i
    c += 1
  if c == 0:
    avg = 0
  else:
    avg = soma / c
  return avg

print(
  """
  Lista de input: {}
  Media: {:.2f}
  Pares
  - Lista: {}
  - Qtd: {}
  - Avg: {}
  Impares
  - Lista: {}
  - Qtd: {}
  - Avg: {}
  """.format(
    lista_input,
    avg(lista_input),
    lista_even,
    len(lista_even),
    avg(lista_even),
    lista_odd,
    len(lista_odd),
    avg(lista_odd),
  )
)
