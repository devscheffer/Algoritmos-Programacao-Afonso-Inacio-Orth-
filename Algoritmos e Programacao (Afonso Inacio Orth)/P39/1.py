#

lista = [1,2,3]
maior = lista[0]
outros = 0

for i in lista:
  if maior < i:
    maior = i

for i in lista:
  if i != maior:
    outros += i

mp = (maior*5 + (outros)*2.5)/10

print("mp {}".format(mp))
