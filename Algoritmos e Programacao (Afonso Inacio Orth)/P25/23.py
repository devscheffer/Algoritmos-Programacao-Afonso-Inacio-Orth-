#

massa = 1
aceleracao = 1
tempo = 30

velocidade_inicial = 0
velocidade_final = aceleracao*tempo + velocidade_inicial

comprimento_pista = velocidade_inicial*tempo + aceleracao*(tempo**2)/2

trabalho_mecanico = massa*(velocidade_final**2)/2

print("""
Velocidade
Inicial: {}
Final: {}
""".format(
  velocidade_inicial,
  velocidade_final
))

print("""
Comprimento da pista: {}
Trabalho mecanico: {}
""".format(
  comprimento_pista,
  trabalho_mecanico
))