#

from random import randint

lista_socio = []

class Socio:
  def __init__(self, name, salario, n_filhos):
    self.name = name
    self.salario = salario
    self.n_filhos = n_filhos

def create_socio(n,lista1):
  c = 0
  while c < n:
    c +=1
    name = "ID {}".format(c)
    salario = randint(0, 1000)
    n_filho = randint(0,10)
    soc = Socio(name, salario, n_filho)
    lista1.append(soc)

def avg(lista_socio):
  soma_salario = 0
  soma_filhos = 0
  count = 0

  for i in lista_socio:
    count += 1
    soma_salario += i.salario
    soma_filhos += i.n_filhos

  avg_salario = soma_salario / count
  avg_filhos = soma_filhos / count
  return avg_salario, avg_filhos

def highest(lista1):
  maior = lista1[0]
  for i in lista1:
    if i.salario > maior.salario:
      maior = i
  return maior.salario

def count_salario(lista1, max):
  c = 0
  for i in lista1:
    if i.salario <= max:
      c += 1
  return c

create_socio(5,lista_socio)

for i in lista_socio:
  print(
    """
    Socio: {}
    Salario: {}
    Numero de filhos: {}
    """.format(
      i.name,
      i.salario,
      i.n_filhos
    ))

print(
  """
  Media salario: {}
  Media de filhos: {}
  Maior salario: {}
  Numero de socios com salario (<= 400): {:.1f} %
  """.format(
    avg(lista_socio)[0],
    avg(lista_socio)[1],
    highest(lista_socio),
    count_salario(lista_socio, 400) / len(lista_socio) * 100
  ))
