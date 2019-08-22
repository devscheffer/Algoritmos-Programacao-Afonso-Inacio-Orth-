#

p = 0
t = 0
v = 10

while t <= 30:
  d = v*t
  print(
    """
    Tempo: {}
    Distancia: {}
    """.format(
      t,
      d
    )
  )
  t += 1
