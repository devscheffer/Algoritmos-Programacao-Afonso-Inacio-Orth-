#

from random import randint

def create_dict(nt,dict):
  c = 0
  while c < nt:
    c += 1
    cod = c
    cod_city = "city {}".format(cod)
    n_veiculos = randint(0,10)
    n_acidentes = randint(0,10)
    dict[cod_city] = n_veiculos,n_acidentes

dict_city = {}
create_dict(20,dict_city)
print(dict_city)

maior = (list(dict_city.values())[0][1])
menor = (list(dict_city.values())[0][1])

for i in dict_city.values():
  if maior < i[1]:
    maior = i[1]
  if menor > i[1]:
    menor = i[1]

def city(type):
  for i in dict_city.items():
    if i[1][1] == type:
      print("- {}".format(i[0]))

print("Maior Indice: {}".format(maior))
city(maior)
print("Menor Indice: {}".format(menor))
city(menor)

def avg (p):
  soma = 0
  c = 0
  for i in dict_city.items():
    soma += i[1][p]
    c += 1
  avg = soma / c
  return avg

print(
  """
  Media de veiculos: {}
  Media de acidentes: {}
  """.format(
    avg(0),
    avg(1)
  )
)
