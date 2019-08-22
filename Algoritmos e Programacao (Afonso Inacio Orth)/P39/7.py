#

lista = [10,20,1]
lista = sorted(lista,reverse = True)

a = lista[0]
b = lista[1]
c = lista[2]
print("""
a = {}
b = {}
c = {}
""".format(
  a,
  b,
  c
))

if a > b + c:
  print("Nao formam triangulo")
elif a**2 == b**2 + c**2:
  print("Formam um triangulo retangulo")
elif a**2 > b**2 + c**2:
  print("Formam um triangulo obtusangulo")
elif a**2 < b**2 + c**2:
  print("Formam um triangulo acutangulo")
elif a == b and b == c:
  print("Formam um triangulo equilatero")
elif a == b or b == c or a == c and a != b or a != c:
  print("Formam um triangulo  isosceles")
