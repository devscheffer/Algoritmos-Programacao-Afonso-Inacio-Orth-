#

funcionario_id = 1
funcionario_idade = 45
tempo_servico = 10

horas_trabalhada = 8
valor_hora = 100
salario_bruto = horas_trabalhada*valor_hora

n_filho_14 = 1
salario_familia_filho = 100

inss = 0.085

if salario_bruto > 1500:
  imposto_renda = 0.15
if salario_bruto > 500 and salario_bruto <= 1500:
  imposto_renda = 0.10
if salario_bruto < 500:
  imposto_renda = 0.00
desconto = salario_bruto*imposto_renda + salario_bruto*inss
print("Imposto de renda: {}".format(desconto))

if funcionario_idade > 40:
  adicional = 0.02
if tempo_servico > 15:
  adicional = 0.035
if tempo_servico < 15 and tempo_servico > 5 and funcionario_idade > 30:
  adicional = 0.015

add = salario_bruto*adicional
print("Adicional: {}".format(add))

print("""
Numero do funcionario: {}
Idade: {}
Salario bruto: {}
Taxa_Imposto de renda: {}
Desconto total: {}
Taxa_Adicional: {}
Adicional: {}
Tempo de servico: {}
Salario liquido: {}
""".format(
  funcionario_id,
  funcionario_idade,
  salario_bruto,
  imposto_renda,
  desconto,
  adicional,
  add,
  tempo_servico,
  salario_bruto - desconto + add
))
