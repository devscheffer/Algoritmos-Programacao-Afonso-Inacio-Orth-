# Texto

n_funcionario = int(input("Numero do funcionario: "))
horas_trabalhadas = float(input("Horas trabalhadas: "))
salario_hora = float(input("Valor por hora (USD): "))
n_filhos = int(input("Numero de filhos com idade menor que 14 anos: "))
salario_familia = float(input("Valor do salario familia: "))

salario = horas_trabalhadas*salario_hora
aux_familia = n_filhos*salario_familia
salario_total = salario + aux_familia

print("""
Salario base: {}
Auxilio familia: {}
Salario total: {}
""".format(
  salario,
  aux_familia,
  salario_total
))

print("Numero de funcionario: {} Salario: {}".format(n_funcionario,salario_total))