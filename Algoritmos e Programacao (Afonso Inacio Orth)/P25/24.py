#

dist_popular = .1
dist_geral = .5
dist_arquibancada = .3
dist_cadeiras = .1

valor_popular = 1
valor_geral = 5
valor_arquibancada = 10
valor_cadeiras = 20

publico = 100
renda = publico*(dist_popular*valor_popular + dist_geral*valor_geral + dist_cadeiras*valor_cadeiras + dist_arquibancada*valor_arquibancada)
print(
"""
Numero de pessoas no jogo {} 
Renda {}
""".format(
  publico,
  renda))
