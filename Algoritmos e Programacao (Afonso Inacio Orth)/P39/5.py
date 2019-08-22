#

x1 = 1
y1 = 1
x2 = 2
y2 = 2
x3 = 1
y3 = 3

def dist(x0, y0, xf, yf):
  d = ((xf - x0)**2 + (yf - y0)**2)**.5
  return d

def triangle(a,b,c):
  if (abs(b - c) < a) and (a < b + c):
    p = (a + b + c)/2
    area = (p*(p-a)*(p-b)*(p-c))**.5
    print("Area: {:.2f}".format(area))
  else:
    print("Nao e um triangulo")
    print("""
    d12: {:.2f}
    d23: {:.2f}
    d31: {:.2f}
    """.format(
      a,
      b,
      c
    ))

d12 = dist(x1, y1, x2, y2)
d23 = dist(x2, y2, x3, y3)
d31 = dist(x3, y3, x1, y1)

triangle(d12, d23, d31)
