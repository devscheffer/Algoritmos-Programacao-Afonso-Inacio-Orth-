#

from random import randint

def create_lista(lista1):
  c = 95
  while c < 1475:
    if primo(c) == 2:
      lista1.append(c)
    c += 1

def primo(n):
  c = 1
  div = 0
  while c <= n:
    if n % c == 0:
      div += 1 
    if n == 1:
      div = 2
    c += 1
  return div

lista_input = []
create_lista(lista_input)
print(lista_input)
prod = 1
for i in lista_input:
  prod *= i
print(prod)