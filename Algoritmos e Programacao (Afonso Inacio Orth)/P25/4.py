#
from math import pi

a = 1
b = 2
c = 3

triangulo = a*b/2
circulo = pi*c**2
trapezio = (a + b)*c/2
quadrado = b**2
retangulo = a*b
superficie_cubo = 6*c**2

print("""
Triangulo: {:.2f}
Circulo: {:.2f}
Trapezio: {:.2f}
Quadrado: {:.2f}
Retangulo: {:.2f}
Superficie do Cubo: {:.2f}
""".format(
  triangulo,
  circulo,
  trapezio,
  quadrado,
  retangulo,
  superficie_cubo
))
