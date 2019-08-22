#

n_vendedor = input("Numero do funcionario: ")
salario_fixo = 1000
valor_carro = []
perc_carro_vendido = .5
n_carro = int(input("Numero de carros vendidos: "))

for i in range(n_carro):
  v_car = float(input("Valor do carro {}: ".format(i+1)))
  valor_carro.append(v_car)

comissao = 0
for i in valor_carro:
  comissao += i
comissao = comissao*perc_carro_vendido
print("Valor da comissao: {}".format(comissao))

salario = salario_fixo + comissao*1.05
print("Vendedor: {} Salario: {}".format(n_vendedor, salario))
