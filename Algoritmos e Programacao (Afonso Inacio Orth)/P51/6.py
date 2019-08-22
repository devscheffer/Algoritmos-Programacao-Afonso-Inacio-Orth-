#

t0 = 0
t1 = 1
lista_fib = []
lista_fib.append(t0)
lista_fib.append(t1)

n_t = 10
fib = 0
p = 0

while p < 10:
  fib = lista_fib[p + 1] + lista_fib[p]
  p += 1
  lista_fib.append(fib)

print(lista_fib)