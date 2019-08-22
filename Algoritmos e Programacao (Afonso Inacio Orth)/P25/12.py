#

custo_fabrica = 1000
perc_distribuidor = 0.1
perc_imposto = 0.1

custo_total = custo_fabrica*(1 + (perc_distribuidor + perc_imposto))

print("Valor do carro: {}".format(custo_total))