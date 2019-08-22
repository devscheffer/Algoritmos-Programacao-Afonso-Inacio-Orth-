#

from random import uniform

def create_dict_prod(nt, dict):
  cod = 0
  while cod < nt:
    cod += 1
    price = round(uniform(0, 100),2)
    dict[cod] = price

def create_list_even_odd(dict):
  for i in dict.items():
      if i[0] % 2 == 0:
        lista_even.append(i)
      else:
        lista_odd.append(i)

dict_prod = {}
create_dict_prod(5,dict_prod)
print(dict_prod)
lista_even = []
lista_odd = []
create_list_even_odd(dict_prod)
print(lista_even)
print(lista_odd)

def corr(lista1, tax, dict):
  for i in range(len(lista1)):
    new_price = lista1[i][1] * (1 + tax)
    new_price = round(new_price,2)
    dict[lista1[i][0]] = [lista1[i][1], tax, new_price]

dict_even = {}
dict_odd = {}

corr(lista_even, 0.15, dict_even)
corr(lista_odd, 0.20, dict_odd)
print(dict_even)
print(dict_odd)

for i in dict_even.items():
  print(
    """
    Codigo: {}
    Preco original: {}
    Preco novo: {}
    Taxa: {}
    """.format(
      i[0],
      i[1][0],
      i[1][2],
      i[1][1]
    )
  )

for j in dict_odd.items():
  print(
    """Codigo: {}
Preco original: {}
Preco novo: {}
Taxa: {}
    """.format(
      j[0],
      j[1][0],
      j[1][2],
      j[1][1]
    )
  )
