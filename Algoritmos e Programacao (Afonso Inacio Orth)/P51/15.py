#

from random import randint

lista_number = []
dict_pair = {}

def create_list_number(ni,nf,t,lista1):
  c = 0
  while c < t:
    a = randint(ni,nf)
    b = randint(ni, nf)
    if a > b:
      a,b = b,a
    c += 1
    lista1.append([a,b])

def soma_between(a,b,dict1):
  result = 0
  name_key = "{},{}".format(a,b)
  dict1[name_key] = []
  while a <= b:
    dict1[name_key].append(a)
    result += a
    a += 1
  return dict_pair[name_key],result

create_list_number(0,10,5,lista_number)

print(dict_pair)
print(lista_number)
for i in lista_number:
  res = soma_between(i[0], i[1], dict_pair)
  print(
    """
    Par: {}
    Pares entre: {}
    Soma dos valores: {}
    """.format(
      i,
      res[0],
      res[1]
    ))

