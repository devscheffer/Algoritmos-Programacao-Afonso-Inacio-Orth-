#

preco_produto = 10
cod_origem = 2

dict_cod = {
  1:"Sul",
  2:"Norte",
  3:"Sudeste",
  4:"Centro-oeste"
  }

def procedencia(cod):
  test = True
  for i in dict_cod.keys():
    if i == cod:
      test = False
      res = dict_cod.get(i)
  if test:
    res = "Importado"
  return res


print("""
Preco do produto: {}
Procedencia: {}
""".format(
  preco_produto,
  procedencia(cod_origem)
  ))
