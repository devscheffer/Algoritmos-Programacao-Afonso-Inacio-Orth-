#

n_vendedor = 1
salario_fixo = 100
vendas = 40000

if vendas <= 10000:
  comissao = 0.03
else:
  comissao = 0.05

print("""
Numero do vendedor: {}
Total de vendas: {}
Salario fixo: {}
Salario total: {}
""".format(
  n_vendedor,
  vendas,
  salario_fixo,
  salario_fixo + vendas*comissao
))