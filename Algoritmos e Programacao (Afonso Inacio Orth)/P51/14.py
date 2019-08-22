#

from random import randint

lista_number = []
dict_even = {}

def create_list_number(ni,nf,t,lista1):
  c = 0
  while c < t:
    a = randint(ni,nf)
    b = randint(ni, nf)
    if a > b:
      a,b = b,a
    c += 1
    lista1.append([a,b])

def check_even(a,b,dict_even):
  name_key = "{},{}".format(a,b)
  dict_even[name_key] = []
  while a <= b:
    if a%2 == 0:
      dict_even[name_key].append(a)
    a += 1
  return dict_even[name_key]
create_list_number(0,10,5,lista_number)

for i in lista_number:
  print(
    """
    Par: {}
    Pares entre: {}
    """.format(
      i,
      check_even(i[0],i[1],dict_even)
    ))

