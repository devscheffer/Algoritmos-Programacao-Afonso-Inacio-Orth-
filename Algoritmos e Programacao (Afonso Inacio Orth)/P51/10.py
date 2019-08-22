# Nao finalizado

from random import randint

lista_number = [13]

def create_list(n,lista_number):
  c = 0
  while c < n:
    v = randint(0,20)
    lista_number.append(v)
    c += 1

create_list(10,lista_number)

def check_even_odd(n):
  if n%2 == 0:
    return n_div(n)
  if n%2 != 0:
    if n < 12:
      return fat(n)
    else:
      return soma(n)

def n_div(n_input):
  div = 0
  v = 1
  while v <= n_input:
    if n_input % v == 0:
      div += 1
    v += 1
  return div

def fat(n):
  res = n
  while n >= 1:
    if n == 1:
      res *= 1
      break
    else:
      res *= (n - 1)
    n -= 1
  return res

def soma(n):
  c = 0
  res = 0
  while c <= n:
    res += c
    c += 1
  return res

print(
  """
  | {:10} | {:10} |
  """.format(
  "Valor m", 
  "Resultado"
  ))
for i in lista_number:
  print(
  """
  | {:10} | {:10} |
  """.format(
    i,
    check_even_odd(i)
    ),end="")
