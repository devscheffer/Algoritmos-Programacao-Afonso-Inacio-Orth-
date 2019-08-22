#

from random import uniform
from random import randint

def create_prod(nt,lista1):
  c = 0
  while c < nt:
    c += 1
    cod_prod = c
    price = round(uniform(0,50),2)
    cod_proc = randint(1,6)
    lista1.append([cod_prod, price, cod_proc])

def find(n):
  ind = lista_cod_proc.index(n)
  return lista_cod_proc_leg[ind]

lista_cod_proc = [1, 2, 3, 4, 5, 6, ]
lista_cod_proc_leg = ["Sul","Sudeste", "Centro-oeste", "Nordeste", "Norte", "Importado"]
lista_frete = [.1,.03,.12,.18,.25,.45]
lista_lucro = [.4,.4,.36,.32,.3,.2]

lista_prod = []
create_prod(3,lista_prod)
print(lista_prod)
prod_final_price = []
for i in lista_prod:
  ind = (lista_cod_proc.index(i[2]))
  final_price = i[1] * (1 + lista_frete[ind]) * (1 + lista_lucro[ind])
  final_price = round(final_price,2)
  prod_final_price.append([i, final_price])
print(prod_final_price)

for i in prod_final_price:
  print(
    """
    Prod: {}
    Valor: {}
    Procedencia: {}
    Valor corrigido: {}
    """.format(
      i[0][0],
      i[0][1],
      find(i[0][2]),
      i[1]
    )
  )
