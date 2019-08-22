#

from random import randint

c = 0
lista_number = []
lista_interval = [0, 25, 50, 75, 100]
lista_interval = sorted(lista_interval)
dict_bar = {}
lista_interval_name = []
lista_avg = []

# Gera lista
while c < 100:
  c += 1
  n = randint(0,100)
  lista_number.append(n)

# Contagem de classe
def bar(n, inf, sup, last):
  if n >= inf and n < sup:
    c = 1
  elif n == last:
    c = 1
  else:
    c = 0
  return c

# Cria nome dos grupos
def create_name_group(lista_interval,p):
    lim_inf = lista_interval[p]
    lim_sup = lista_interval[p + 1]
    grupo = "{}-{}".format(lim_inf, lim_sup)
    lista_interval_name.append(grupo)
    return lim_inf, lim_sup, grupo

# Cria dicionario dos grupos
def create_dict(lista_interval):
  for j in range(len(lista_interval) - 1):
    grupo = create_name_group(lista_interval, j)
    dict_bar[grupo[2]] = [0,[],0]

# Classifica os valores i da lista
def grupo_classification(lista_number, lista_interval):
  for i in lista_number:
    for j in range(len(lista_interval) - 1):
      grupo = create_name_group(lista_interval, j)
      count = bar(i, grupo[0], grupo[1],lista_interval[-1])
      dict_bar[grupo[2]][0] += count
      if count == 1:
        dict_bar[grupo[2]][1].append(i)

def avg(dict0, dict1):
  soma = 0
  for k in dict1:
    soma += k
  if dict0 == 0:
    avg = 0
  else:
    avg = soma/dict0
  return avg

create_dict(lista_interval)
grupo_classification(lista_number, lista_interval)

for i in lista_interval_name:
  avg1 = avg(dict_bar[i][0], dict_bar[i][1])
  dict_bar[i][2] = avg1

print(" Total de valores: {}".format(len(lista_number)))
for k in dict_bar.items():
  print(
  """
  Grupo: {}
  Frequencia: {}
  Percentual: {:.1f} %
  Media do grupo: {:.2f}
  Lista:
  {}
  """.format(
    k[0],
    k[1][0],
    k[1][0]/len(lista_number)*100,
    k[1][2],
    k[1][1]
    ))

print(
"""
| {:9} | {} | {} | {} |
""".format(
  "Grupo",
  "Frequencia",
  "Percentual",
  "Media do grupo"
  ))
for k in dict_bar.items():
  print(
"""
| {:9} | {:10} | {:10.2f} | {:14.2f} |
""".format(
    k[0],
    k[1][0],
    k[1][0]/len(lista_number)*100,
    k[1][2]
),end="")
