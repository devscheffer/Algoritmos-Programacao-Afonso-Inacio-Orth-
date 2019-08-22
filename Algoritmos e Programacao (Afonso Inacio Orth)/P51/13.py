#

from random import randint

lista_number = [0]
dict_n = {}

def create_list_number(ni,nf,t,lista1):
  c = 0
  while c < t:
    n = randint(ni,nf)
    c += 1
    lista1.append(n)

def create_tab(n,dict_n):
  c = 0
  dict_n[n] = []
  while c <= n:
    tab = c * n
    dict_n[n].append([c,tab])
    c += 1


create_list_number(0,10,10,lista_number)
for i in lista_number:
  create_tab(i,dict_n)

for j in dict_n.items():
  print(
    """
    {}
    Valor n: {}
      | {:15} | {:15} |
    """.format(
      "="*10,
      j[0],
      "Multiplicador",
      "Resultado"
    ),end="")
  for k in j[1]:
    print(
    """
      | {:15} | {:15} |
    """.format(
      k[0],
      k[1]
    ), end="")
