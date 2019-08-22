#

from random import randint

def create_lista(nt, lista1):
  c = 0
  while c < nt:
    n = randint(0,10)
    lista1.append(n)
    c += 1

lista_input = []
create_lista(3,lista_input)
print(lista_input)

n = 0
dict_s = {}
for i in lista_input:
  dict_s[i] = []
  while n < i:
    n += 1
    dict_s[i].append(round(1/n,2))
  n = 0
  soma = 0
  for j in dict_s[i]:
    soma += j
  soma = round(soma,2)
  dict_s[i] = dict_s[i],soma
  
for i in dict_s.items():
  print(
    """Valor S: {}
    Lista dos termos S: {}
    Soma dos termos: {}
    """.format(
      i[0],
      i[1][0],
      i[1][1]
    )
    )

