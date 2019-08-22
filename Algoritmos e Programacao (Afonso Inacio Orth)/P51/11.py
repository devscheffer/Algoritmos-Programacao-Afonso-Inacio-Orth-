#

from random import randint

lista_number = []

def create_list(ri, rf, n, lista_number):
  c = 0
  while c < n:
    v = randint(ri,rf)
    lista_number.append(v)
    c += 1

def media(lista1):
  c = 0
  total = 0
  for i in lista1:
    c += 1
    total += i
  med = total/c
  return med

def count_even_odd(lista1):
  odd = 0
  even = 0
  for i in lista1:
    if i%2 == 0:
      even += 1
    else:
      odd += 1
  return even,odd

create_list(0,10,5,lista_number)
resm = media(lista_number)
resc = count_even_odd(lista_number)
totalc = len(lista_number)

print(lista_number)
print(
  """
  Media aritmetica: {}
  Qtd even: {} ({}%)
  Qtd odd: {} ({}%)
  """.format(
    resm,
    resc[0],
    resc[0]/totalc*100,
    resc[1],
    resc[1]/totalc*100
  ))
