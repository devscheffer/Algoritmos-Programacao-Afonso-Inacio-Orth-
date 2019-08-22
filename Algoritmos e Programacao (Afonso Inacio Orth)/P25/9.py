#

salario = 123
notas = [100,50,10,5,1]
notas = sorted(notas, reverse = True)

def n_notas(salario,valor):
  qtd_notas = int(salario/valor)
  resto = salario - qtd_notas*valor
  return qtd_notas,resto

valor = salario
print("Salario: {}".format(salario))
for i in notas:
  resultado = n_notas(valor, i)
  print("""Qtd de notas valor {:3d}: {}"""
  .format(
    i,
    resultado[0]
  ))
  valor = resultado[1]