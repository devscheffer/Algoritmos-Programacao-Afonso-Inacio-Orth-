#

dia_taxa = 10
km_taxa = 5
dia = 10
km = 100
desconto = .1

aluguel = dia*dia_taxa*(1 - desconto) + km*km_taxa

print("""
Aluguel: {}
Desconto: {}
Numero de dias: {}
km rodado: {}
""".format(
  aluguel,
  desconto,
  dia,
  km
))