#

from random import randint

def create_lista_input(lista_input):
  n = randint(1,3)
  c = 0

  while c < n:
    n2 = randint(0,10)
    c += 1
    lista_input.append(n2)

  print(n)
  print(lista_input)

def fat(n):
  c = n

  while c > 1:
    n *= (c - 1)
    c -= 1
  return n

lista_input = []
create_lista_input(lista_input)
for i in lista_input:
  print(
    """
    Valor: {}
    Fatorial: {}
    Raiz cubica: {:.2f}
    """.format(
      i,
      fat(i),
      i**(1/3)
    )
  )