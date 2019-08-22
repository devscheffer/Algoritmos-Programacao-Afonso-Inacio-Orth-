#

from random import randint

n = randint(0,10)

def fat(n):
  res = n
  if n == 0:
    res = 1
  while n > 1:
    res *= (n - 1)
    n -= 1
  return res

def e(n):
  c = 0
  ev = 0
  while c <= n:
    ev += 1/(fat(c))
    c += 1
  return ev

print(
  """
  n: {}
  e: {:.2f}
  """.format(
    n,
    e(n)
    ))