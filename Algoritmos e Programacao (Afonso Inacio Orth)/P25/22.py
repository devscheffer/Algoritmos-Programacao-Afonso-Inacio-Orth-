#

qtd_farinha = 1
qtd_agua = 1
qtd_fermento = 1
qtd_kWh = 1

custo_farinha = 1
custo_agua = 1
custo_fermento = 1
custo_kWh = 1

imposto = .3
lucro = .3

custo_pao = (qtd_agua*custo_agua + qtd_farinha*custo_farinha + qtd_fermento*custo_fermento + qtd_kWh*custo_kWh)*(1 + imposto)

venda_pao = custo_pao*(1 + lucro)

print("""
Pao
Custo: {:.2f}
Venda: {:.2f}
""".format(custo_pao,venda_pao))
