  #

from random import randint

def create_list_number(ni,nf,t,lista1,lista_cod):
  c = 0
  while c < t:
    n = randint(ni,nf)
    cod = lista_cod[randint(0,len(lista_cod)-1)]
    c += 1
    lista1.append([cod,n])

def count_total(lista1):
  c = 0
  for i in lista1:
    c += i[1]
  return c

def count_cat(lista_number, lista_cod, dict_cat):
  for i in lista_number:
    for j in lista_cod:
      if i[0] == j:
        dict_cat[j] += i[1]

lista_number = []
lista_cod = [1,2]
dict_cat = {}
for j in lista_cod:
  dict_cat[j] = 0

create_list_number(1,10,5,lista_number,lista_cod)
count_cat(lista_number,lista_cod,dict_cat)
print(lista_number)
print(len(lista_number))
print(
  """
  Total de cobaias: {}
  """.format(
    count_total(lista_number)
    ),end="")
for i in dict_cat.items():
  print(
    """
    Categoria: {}
    Numero de cobais: {} ({:.1f} %)
    """.format(
      i[0],
      i[1],
      i[1] / count_total(lista_number) * 100
      ),end="")
