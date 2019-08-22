#

id_aluno = 1
n1 = 6
n2 = 8
n3 = 8
me = 9

ma = (n1 + n2*2 + n3*3 + me)/7

if ma >= 9:
  conceito = ("A")
elif ma >= 7.5:
  conceito = ("B")
elif ma >= 6:
  conceito = ("C")
elif ma >= 4:
  conceito = ("D")
elif ma < 4:
  conceito = ("E")

if conceito == "A" or conceito == "B" or conceito == "C":
  situacao = ("Aprovado")
if conceito == "D" or conceito == "E":
  situacao = ("Reprovado")

print("""
Numero do aluno: {}
Nota 1: {:.2f}
Nota 2: {:.2f}
Nota 3: {:.2f}
Media dos exercicios: {:.2f}
Media de aproveitamento: {:.2f}
Conceito: {}
Situacao: {}
""".format(
  id_aluno,
  n1,
  n2,
  n3,
  me,
  ma,
  conceito,
  situacao
))
