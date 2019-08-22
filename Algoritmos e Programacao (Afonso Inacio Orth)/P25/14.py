#

n_funcionario = 10
salario_atual = 1000
intemp = 10
ind_produtividade = 0.5

aumento = intemp*.8 + ind_produtividade*salario_atual
salario = salario_atual + aumento

print("""Numero de funcionarios: {} 
Aumento: {} 
Novo Salario: {}""".format(
  n_funcionario,
  aumento,
  salario
))

