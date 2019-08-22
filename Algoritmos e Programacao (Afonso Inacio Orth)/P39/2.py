#

a = 3
b = 4
c = 5

if (abs(b - c) < a) and (a < b + c):
  p = (a + b + c)/2
  area = (p*(p-a)*(p-b)*(p-c))**.5
  print("Area: {}".format(area))
else:
  print("Nao e um triangulo")
