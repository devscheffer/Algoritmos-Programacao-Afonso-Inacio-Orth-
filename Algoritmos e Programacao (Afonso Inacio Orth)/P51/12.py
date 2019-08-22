#

ri = 100
rf = 200

lista_primo = []
lista_number = []

def primo(n,lista1):
  c = 2
  div = 0
  while c <= n:
    if n%c == 0:
      div += 1
    c += 1
  if div == 1 or n == 1:
    lista1.append(n)

def soma(lista1):
  res = 0
  for i in lista1:
    res += i
  return res

def create_number(ni, nf, p, lista1):
  res = 0
  while ni <= nf:
    lista1.append(ni)
    res += ni
    ni += p

create_number(1,10,1,lista_number)
for i in lista_number:
  primo(i,lista_primo)
res_soma = soma(lista_primo)

print(
  """
  Primo: {}
  Soma dos primos: {}
  """.format(
    lista_primo,
    res_soma
  )
)