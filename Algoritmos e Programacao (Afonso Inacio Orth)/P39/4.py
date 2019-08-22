#

lista = [10,2,5,]

while True:
  i = int(input("Valor i: "))
  if i == 1:
    lista_cresc = sorted(lista)
    print("Crescente {}".format(lista_cresc))
  elif i == 2:
    lista_decres = sorted(lista, reverse=True)
    print("Decrescente {}".format(lista_decres))
  elif i == 3:
    maior = lista[0]
    for i in lista:
      if maior < i:
        maior = i
    aux = lista[1]
    lista[1] = maior
    lista[lista.index(maior)] = aux
    print("Lista {}".format(lista))
  else:
    print("Valor invalido de i: {}".format(i))
