#

from random import randint

def create_lista_gabarito(nt,lista1):
  c = 0
  while c < nt:
    c += 1
    n = randint(1, 2)
    lista1.append(n)

def create_dict_aluno(nt,dict):
  c = 0
  while c < nt:
    c += 1
    a1 = randint(1, 2)
    a2 = randint(1, 2)
    a3 = randint(1, 2)
    a4 = randint(1, 2)
    a5 = randint(1, 2)
    name = "Aluno {}".format(c)
    dict[name] = [a1, a2, a3, a4, a5]

lista_gabarito = []
create_lista_gabarito(5,lista_gabarito)
dict_aluno = {}
create_dict_aluno(5,dict_aluno)
print(lista_gabarito)
print(dict_aluno)
print(dict_aluno.values())

for i in range(len(lista_gabarito)):
  for j in dict_aluno.items():
    print("i: {} j: {}".format(i,j[1]))
    if lista_gabarito[i] == j[1][i]:
      dict_aluno[j[0]][i] = [j[1][i], "Certo"]
    else:
      dict_aluno[j[0]][i] = [j[1][i], "Errado"]

q = 0
for i in dict_aluno.items():
  print("""\n{}""".format(i[0]))
  c = 0
  e = 0
  for j in i[1]:
    q += 1
    print("Questao: {} Resposta: {} Resultado: {}".format(q, j[0], j[1]))
    if j[1] == "Certo":
      c +=1
    else:
      e += 1
  print(
    """Acertos: {0}/{2}
Erros: {1}/{2}
    """.format(
      c,
      e,
      c + e
      ))
  q = 0
