#

t0 = 0
t1 = 1
lista_fib = []
lista_fib.append(t0)
lista_fib.append(t1)

n_t = 10
fib = 0
p = 1

while p < 10:
  fib = lista_fib[p] + lista_fib[p - 1]
  lista_fib.append(fib)
  p += 1

for i in lista_fib:
  print("{:3} - {}".format(lista_fib.index(i), lista_fib[lista_fib.index(i)]))
