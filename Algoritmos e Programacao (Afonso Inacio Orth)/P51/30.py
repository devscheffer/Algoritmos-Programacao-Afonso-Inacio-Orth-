#

from random import randint
from random import uniform


def create_dict_people(nt, dict):
  c = 0
  while c < nt:
    c += 1
    age = randint(0, 90)
    sex = randint(0, 1)
    if sex == 0:
      sex = "f"
    else:
      sex = "m"
    salary = round(uniform(0,1000),2)
    name = "Person {}".format(c)
    dict[name] = [age,sex,salary]



def avg(dict_people):
  soma = 0
  c = 0
  for i in dict_people.items():
    soma += i[1][2]
    c += 1
  avg = soma / c
  return avg

def age_maior(dict):
  lista1 = []
  for i in dict.items():
    lista1.append(i[1][0])
  maior = lista1[0]
  for j in lista1:
    if maior < j:
      maior = j
  return maior

def age_menor(dict):
  lista1 = []
  for i in dict.items():
    lista1.append(i[1][0])
  menor = lista1[0]
  for j in lista1:
    if menor > j:
      menor = j
  return menor

def cat_sal(cat, sal):
  nf = 0
  for i in dict_people.values():
    print(i)
    if i[1] == cat and i[2] <= sal:
      nf += 1
  return nf

dict_people = {}
create_dict_people(4,dict_people)
print(dict_people)
print(
  """
  Media dos salarios: {:.2f} BRL
  Maior idade: {} anos
  Menor idade: {} anos
  Mulheres com salario até 500 BRL: {}
  """.format(
    avg(dict_people),
    age_maior(dict_people),
    age_menor(dict_people),
    cat_sal("f",500)
  )
)
