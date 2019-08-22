#

n_apartamento = 42
ocupacao_normal_taxa = .4
ocupacao_promo_taxa = .7
ocupacao_normal = int(n_apartamento*ocupacao_normal_taxa)
ocupacao_promo = int(n_apartamento*ocupacao_promo_taxa)

diaria_normal = 100
taxa_promo = 0.22
diaria_promo = diaria_normal*(1 - taxa_promo)

dias = 8

print("""
Valor da diaria
Normal: {}
Promocional: {}
""".format(
  diaria_normal,
  diaria_promo
))


arrecadacao_normal = dias*diaria_normal*ocupacao_normal
arrecadacao_promo = dias*diaria_promo*ocupacao_promo

print("""
Numero de quartos ocupados
Sem promocao: {}
Com promocao: {}

Valor arrecado durante um mes
Sem promocao: {:.2f}
Com promocao: {:.2f}
""".format(
  ocupacao_normal,
  ocupacao_promo,
  arrecadacao_normal,
  arrecadacao_promo
))

final = arrecadacao_promo - arrecadacao_normal
print("Com a promocao foi obtido:")
if final > 0:
  print("Lucro de {:.2f}".format(
    final
  ))
else:
  print("Prejuizo: {:.2f}".format(
    final
  ))
