  #

from random import randint


def create_lista_input(t, lista_input):
  c = 0
  while c < t:
    salario = randint(500,2000)
    total_vendas = randint(2000,15000)
    c += 1
    lista_input.append([salario,total_vendas])

lista_input = []
create_lista_input(5,lista_input)
print(lista_input)


def vendedor(lista_input, dict_vendedor):
  id = 0
  for i in lista_input:
    id += 1
    name = "Vendedor {}".format(id)
    dict_vendedor[name] = i
dict_vendedor = {}
vendedor(lista_input,dict_vendedor)
print(dict_vendedor)

def comissao(vendas):
  if vendas <= 10000:
    com = 0.03
  else:
    com = 0.05
  return com

for i in dict_vendedor.items():
  print(
    """
    {}
    Salario base: {} BRL
    Vendas: {} BRL
    Comissao: {:.1f} %
    Salario total: {:.2f} BRL
    """.format(
      i[0],
      i[1][0],
      i[1][1],
      comissao(i[1][1]) * 100,
      i[1][0] + (i[1][1] * comissao(i[1][1]))
    ))
