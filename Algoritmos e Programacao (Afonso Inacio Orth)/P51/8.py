#

lista_fib = []
n_t = 10

def create_fib(n_t,lista_fib):
  lista_fib.append(0)
  lista_fib.append(1)
  fib = 0
  p = 1
  while p < n_t:
    fib = lista_fib[p] + lista_fib[p - 1]
    lista_fib.append(fib)
    p += 1

def check_primo(n_input):
  v = 2
  div = 0
  while v <= n_input:
    if n_input%v == 0:
      div += 1
    v += 1
  if div == 1:
    status = "True"
  else:
    status = "False"
  return status

create_fib(n_t, lista_fib)
print("| {:^9} | {:^9} | {:^9} |".format("Numero", "Posicao", "Primo"))
for i in range(len(lista_fib)):
  stat = check_primo(i)
  print("| {:9} | {:9} | {:^9} |".format(lista_fib[i], i, stat))
