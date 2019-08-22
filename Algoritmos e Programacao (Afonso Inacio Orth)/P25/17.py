#

valor_dolar = 100
taxa_dolar = 4
perc_icms = .5
lucro = .1

valor_real = valor_dolar*taxa_dolar*(1 + (perc_icms + lucro))
print("Valor em dolar: {} Valor em real: {}".format(valor_dolar,valor_real))