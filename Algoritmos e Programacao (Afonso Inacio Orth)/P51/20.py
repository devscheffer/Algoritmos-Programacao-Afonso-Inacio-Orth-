#

from random import randint

def create_list_number(ni,nf,t,lista1):
  c = 0
  while c < t:
    n = randint(ni,nf)
    c += 1
    lista1.append(n)

def create_urna(lista1):
  for i in lista1:
    dict_votos[i] = 0
  dict_votos["Nulo"] = 0
  dict_votos["Branco"] = 0

def cont_votos(lista1,lista2,dict1):
  for i in lista1:
    if i in lista2:
      dict1[i] += 1
    if i == -1:
      dict1["Nulo"] += 1
    if i == 0:
      dict1["Branco"] += 1

lista_cod_candidato = [1,2,3,4]
lista_votos = []
dict_votos = {}
create_list_number(-1,6,10,lista_votos)
create_urna(lista_cod_candidato)
cont_votos(lista_votos,lista_cod_candidato,dict_votos)

total = 0
for i in dict_votos.values():
  total += i
print(f"Total de votos: {total}")
for i in dict_votos.items():
  print(
    """
    Votos para {}
    Total: {}
    Total: {:.1f} %
    """.format(
        i[0],
        i[1],
        i[1] / total * 100
    ),end="")
