#

from random import randint

dict_aluno = {}

def create_dict(ni,nf,t1,dict1,t2):
  c1 = 0
  c2 = 0
  while c2 < t2:
    c2 += 1
    name = "ID {}".format(c2)
    dict1[name] = []
    while c1 < t1:
      a = randint(ni,nf)
      c1 += 1
      dict1[name].append(a)
    c1 = 0

def mp(lista1):
  lista2 = sorted(lista1,reverse = True)
  c = 0
  res = 0
  for i in lista2:
    if c == 0:
      res += i*4
    else:
      res += i*3
    c += 1
  res = res/10
  return res

def status(n):
  if n >= 5:
    return "Aprovado"
  else:
    return "Reprovado"
create_dict(0,10,3,dict_aluno,3)

for i in dict_aluno.items():
  print(
    """
    Aluno: {}
    Notas: {}
    Media Ponderada: {:.2f}
    Situacao: {}
    """.format(
      i[0],
      i[1],
      mp(i[1]),
      status(mp(i[1]))
    )
  )
