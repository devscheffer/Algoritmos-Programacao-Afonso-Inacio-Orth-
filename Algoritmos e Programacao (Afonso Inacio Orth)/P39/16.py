#

class Cliente:
  def __init__(self, cliente_c1, cliente_c2, cliente_c3):
    self.cliente_c1 = cliente_c1
    self.cliente_c2 = cliente_c2
    self.cliente_c3 = cliente_c3

c1_preco = 10
c2_preco = 1
c3_preco = 1

c1_limit = 18
c2_limit = 12
c3_limit = 6

promo = 0.5

cliente1 = Cliente(20, 0, 0)

def check_c(cliente_pedido, limit, preco):
  if limit >= cliente_pedido:
    pag = cliente_pedido*(1 - promo)*preco
  else:
    pag = limit*(1 - promo)*preco + (cliente_pedido - limit)*preco
  return pag


pagamento_total = check_c(cliente1.cliente_c1, c1_limit, c1_preco) + check_c(cliente1.cliente_c2, c2_limit, c2_preco) + check_c(cliente1.cliente_c3, c3_limit, c3_preco)

print("""
Cerveja tipo 1: {}
Cerveja tipo 2: {}
Cerveja tipo 3: {}
Pagamento: {}
""".format(
  cliente1.cliente_c1,
  cliente1.cliente_c2,
  cliente1.cliente_c3,
  pagamento_total
))
