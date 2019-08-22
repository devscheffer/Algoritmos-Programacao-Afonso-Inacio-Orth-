#

from random import randint
from random import uniform


def create_dict_pop(nt, dict):
  c = 0
  while c < nt:
    c += 1

    age = randint(0, 30)
    
    sex = randint(0, 1)
    if sex == 0:
      sex = "f"
    else:
      sex = "m"

    eyes = randint(1,3)
    if eyes == 1:
      eyes = "Azul"
    elif eyes == 2:
      eyes = "Verde"
    elif eyes == 3:
      eyes = "Castanho"

    hair = randint(1, 3)
    if hair == 1:
      hair = "Loiro"
    elif hair == 2:
      hair = "Preto"
    elif hair == 3:
      hair = "Castanho"

    name = "Person {}".format(c)
    dict[name] = [age,sex,eyes,hair]

def age_maior(dict):
  lista1 = []
  for i in dict.items():
    lista1.append(i[1][0])
  maior = lista1[0]
  for j in lista1:
    if maior < j:
      maior = j
  return maior

def cat():
  nf = 0
  for i in dict_pop.values():
    print(i)
    if i[1] == "f" and i[0] >= 18 and i[0] <= 24 and i[2] == "Verde" and i[3] == "Loiro":
      nf += 1
  return nf

dict_pop = {}
create_dict_pop(525,dict_pop)
print(dict_pop)
print(
  """
  Maior idade: {}
  Mulheres, idade [18-24], olhos [Verdes] e cabelos [Loiros]: {}
  """.format(
    age_maior(dict_pop),
    cat()
  )
)