#

i = int(input("Codigo i: "))
a = 1
b = 5
c = 3

print("""
  a: {}
  b: {}
  c: {}
  """.format(
    a,
    b,
    c
  ))

if i == 1:
  area = (a + b)*c/2
  print("""
  Area do trapezio: {:.2f}
  """.format(
    area
  ))

if i == 2:
  delta = b**2 - 4*a*c
  x1 = (-b + delta**.5)/(2*a)
  x2 = (-b - delta**.5)/(2*a)
  print("""
  Equacao: {}*x**2 + {}*x + {}
  Raiz 1: {:.2f}
  Raiz 2: {:.2f}
  """.format(
    a,
    b,
    c,
    x1,
    x2
  ))

if i == 3:
  mg = (a*b*c)**(1/3)
  print("""
  Media Geometrica: {:.2f}
  """.format(
    mg
  ))

if i == 4:
  sp = (a + b + c)/2
  area = (sp*(sp - a)*(sp - b)*(sp - c))**0.5
  print("""
  Area do triangulo: {:.2f}
  """.format(
    area
  ))
if i > 4:
  print("Codigo Invalido")
