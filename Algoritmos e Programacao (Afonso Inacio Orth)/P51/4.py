#

from random import randint

c = 0
lista_number = []
lista_interval = [0, 25, 50, 75, 100]
lista_interval = sorted(lista_interval)
dict_bar = {}

# Gera lista
while c < 100:
  c += 1
  n = randint(0,100)
  lista_number.append(n)

# Contagem de classe
def bar(n, inf, sup):
  if n >= inf and n < sup:
    c = 1
  else:
    c = 0
  return c

# Cria dicionario dos grupos
def create_dict(lista_interval):
  for j in range(len(lista_interval) - 1):
    lim_inf = lista_interval[j]
    lim_sup = lista_interval[j + 1]
    grupo = "{}-{}".format(lim_inf, lim_sup)
    dict_bar[grupo] = 0

# Classifica os valores i da lista
def grupo_classification(lista_number, lista_interval):
  for i in lista_number:
    for j in range(len(lista_interval) - 1):
      lim_inf = lista_interval[j]
      lim_sup = lista_interval[j + 1]
      count = bar(i, lim_inf, lim_sup)
      grupo = "{}-{}".format(lim_inf, lim_sup)
      dict_bar[grupo] += count


create_dict(lista_interval)
grupo_classification(lista_number, lista_interval)
for k in dict_bar.items():
  print("{:7}: {}".format(k[0],k[1]))
