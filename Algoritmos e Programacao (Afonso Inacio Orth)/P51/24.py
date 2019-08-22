#

from random import uniform


def create_lista_input(t, lista_input):
  c = 0
  while c < t:
    c += 1
    n1 = uniform(0,3)
    n1 = round(n1,2)
    lista_input.append([c,n1])

lista_input = []
create_lista_input(5,lista_input)

maior = lista_input[0][1]
menor = lista_input[0][1]
aluno_maior = lista_input[0][0]
aluno_menor = lista_input[0][0]


for i in lista_input:
  if maior < i[1]:
    maior = i[1]
    aluno_maior = i[0]
  elif menor > i[1]:
    menor = i[1]
    aluno_menor = i[0]

print(
  """
  Maior aluno
  {} com {} m
  Menor aluno
  {} com {} m
  """.format(
    aluno_maior,
    maior,
    aluno_menor,
    menor
  ))
