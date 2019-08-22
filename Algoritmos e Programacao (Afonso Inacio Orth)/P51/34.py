#

from random import randint

def create_lista(lista1):
  c = 1000
  while c <= 2000:
    lista1.append(c)
    c += 1

lista_input = []
lista_output = []
create_lista(lista_input)
print(lista_input)

for i in lista_input:
  if i % 11 == 5:
    lista_output.append([i, "{} * 11 + 5".format(i // 11)])

print("Divisores de 11 com resto igual a 5")
for i in lista_output:
  print(i)