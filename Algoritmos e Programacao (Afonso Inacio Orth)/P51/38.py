#

from random import uniform
from random import randint

def create_lista(nt, lista1):
  c = 0
  while c < nt:
    h = round(uniform(0,3),2)
    cod = randint(1,2)
    if cod == 1:
      cod = "M"
    else:
      cod = "F"
    lista1.append([h,cod])
    c += 1

lista_input = []
create_lista(50,lista_input)
print(lista_input)

dict_pop = {}

def create_dict_cat(dict_pop,cat):
  dict_pop[cat] = []
  for i in lista_input:
    if i[1] == cat:
      dict_pop[cat].append(i[0])

create_dict_cat(dict_pop,"F")
create_dict_cat(dict_pop, "M")
print(dict_pop)


def age_maior(lista1):
  maior = lista1[0]
  for j in lista1:
    if maior < j:
      maior = j
  return maior


def age_menor(lista1):
  menor = lista1[0]
  for j in lista1:
    if menor > j:
      menor = j
  return menor


for i in dict_pop.keys():
  soma = 0
  c = 0
  for j in [dict_pop[i]]:
    maior = age_maior(j)
    menor = age_menor(j)
  dict_pop[i] = dict_pop[i], maior, menor

print(dict_pop)
for i in dict_pop.keys():
  print(
    """
    Sex: {}
    Altura
    - Maior: {}
    - Menor: {}
    """.format(
      i,
      dict_pop[i][1],
      dict_pop[i][2]
    )
  )