# Texto

a = 1
b = 2
c = 3

ma = (a + b + c)/3
mh = 3/(1/a + 1/b + 1/c)
mg = (a*b*c)**(1/3)
mp = (1*a + 2*b + 3*c)/(1 + 2 + 3)

print("""
ma: {:.2f}
mh: {:.2f}
mg: {:.2f}
mp: {:.2f}
""".format(
  ma,
  mh,
  mg,
  mp
))
