#

lista_pessoas = []

class Pessoa:
  def __init__(self, name, height, grow):
    self.name = name
    self.height = height
    self.grow = grow

dict_p = {"Gustavo": [1.4,0.08], "Juliano": [1.1,0.17]}

for i in dict_p.items():
  lista_pessoas.append(Pessoa(i[0],i[1][0],i[1][1]))

n = lista_pessoas[1].height
meta = lista_pessoas[0].height
year = 0

while n < meta:
  n += lista_pessoas[1].grow
  meta += lista_pessoas[0].grow
  year += 1

print(
  f"""
  Anos: {year}

  | {"Nome":^10} | {"Altura":^10} | {"Grow":^10} |
  """, end=""
)

for i in lista_pessoas:
  print(
  f"""
  | {i.name:10} | {i.height:10} | {i.grow:10} |
  """, end=""
  )
