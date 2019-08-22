#

from random import randint
from random import uniform

def create_dict(nt,dict):
  c = 0
  while c < nt:
    c += 1
    sex = randint(0,1)
    if sex == 0:
      sex = "F"
    else:
      sex = "M"
    age = randint(0,90)
    height = round(uniform(1,3),2)
    k = "Person {}".format(c)
    dict[k] = sex,age,height

def avg_group(p):
  soma = 0
  c = 0
  for i in dict_pop.items():
    soma += i[1][p]
    c += 1
  avg = soma / c
  return avg


def avg_cat_f(p):
  soma = 0
  c = 0
  for i in dict_pop.items():
    if i[1][0] == "F":
      soma += i[1][p]
      c += 1
  try:
    avg = soma / c
  except:
    avg = 0
  return avg


def avg_cat_m(p):
  soma = 0
  c = 0
  for i in dict_pop.items():
    if i[1][0] == "M":
      soma += i[1][p]
      c += 1
  try:
    avg = soma / c
  except:
    avg = 0
  return avg


def avg_cat_2153():
  soma = 0
  c = 0
  for i in dict_pop.items():
    if i[1][1] >= 21 and i[1][1] <= 53:
      soma += i[1][1]
      c += 1
  try:
    avg = soma / c
  except:
    avg = 0
  return avg,c

dict_pop = {}
create_dict(2,dict_pop)
print(dict_pop)

print(
  """
  Media de idade: {}
  Media de altura das mulheres: {}
  Media de idade dos homens: {}
  Pessoas com idade [21-53]: {} ({} %)
  """.format(
    avg_group(1),
    avg_cat_f(2),
    avg_cat_m(1),
    avg_cat_2153()[1],
    avg_cat_2153()[1] / len(dict_pop) * 100
  )
)
