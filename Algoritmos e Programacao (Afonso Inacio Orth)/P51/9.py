#

from random import randint

lista_number = []

def create_list(n,lista_number):
  c = 0
  while c < n:
    v = randint(0,10)
    lista_number.append(v)
    c += 1

def create_row(n):
  print(
  """
  | {:8} | {:8} | {:8} | {:8.2f} |
  """.format(
      n,
      n**2,
      n**3,
      n**0.5
      ), end="")

create_list(10,lista_number)
print(
  """
  | {:8} | {:8} | {:8} | {:8} |
  """.format(
    "Valor",
    "Quadrado",
    "Cubo",
    "Raiz"
    ), end="")
for i in lista_number:
  create_row(i)
print(lista_number)
