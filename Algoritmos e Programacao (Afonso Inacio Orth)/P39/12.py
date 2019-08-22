#

n_funcionario = 1
salario = 100

if salario > 2500:
  indice_aumento = 0
elif salario > 1800:
  indice_aumento = 0.04
elif salario > 1000:
  indice_aumento = 0.07
elif salario > 700:
  indice_aumento = 0.10
elif salario > 400:
  indice_aumento = 0.12
else:
  indice_aumento = 0.15

print("""
Numero do funcionario: {}
Salario atual: {:.2f}
Percentual de aumento: {:.2f}
Salario corrigido: {:.2f}
""".format(
  n_funcionario,
  salario,
  indice_aumento,
  salario*(1 + indice_aumento)
))
